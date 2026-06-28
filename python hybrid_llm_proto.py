# hybrid_llm_proto_no_numpy.py
import random

class TokenModel:
    def __init__(self, vocab_size=100, hidden_dim=32):
        self.vocab_size = vocab_size
        self.hidden_dim = hidden_dim

    def step(self, token_id, context_state):
        # random "hidden state"
        h_next = [random.uniform(-1, 1) for _ in range(self.hidden_dim)]
        # random "logits"
        logits = [random.uniform(-1, 1) for _ in range(self.vocab_size)]
        return h_next, logits


class PacketState:
    def __init__(self, dim):
        self.vec = [0.0] * dim

    def update(self, aggregated_hidden, field_state):
        new_vec = []
        for a, f in zip(aggregated_hidden, field_state.vec):
            new_vec.append(self.vec[len(new_vec)] + 0.1 * a + 0.05 * f)
        self.vec = new_vec
        return self.vec

    def bias_logits(self, logits):
        mean_val = sum(self.vec) / len(self.vec)
        scale = (2 / (1 + pow(2.71828, -2 * mean_val))) - 1  # tanh approx
        return [x + scale for x in logits]


class TeleodynamicField:
    def __init__(self, dim):
        self.vec = [0.0] * dim

    def update(self, packet_state, instructions_vec):
        new_vec = []
        for p, i in zip(packet_state.vec, instructions_vec):
            new_vec.append(self.vec[len(new_vec)] + 0.01 * p + 0.1 * i)
        self.vec = new_vec
        return self.vec


class RetardedContext:
    def __init__(self, hidden_dim=32, window=5):
        self.hidden_dim = hidden_dim
        self.window = window
        self.buffer = []

    def update(self, h_t):
        self.buffer.append(h_t)
        if len(self.buffer) > self.window:
            self.buffer.pop(0)

    @property
    def state(self):
        if not self.buffer:
            return [0.0] * self.hidden_dim
        # mean without numpy
        out = []
        for i in range(self.hidden_dim):
            s = sum(h[i] for h in self.buffer)
            out.append(s / len(self.buffer))
        return out


def generate(token_model, packet_state, field_state,
             instructions_vec, max_tokens=40, packet_size=8):

    ret_ctx = RetardedContext(hidden_dim=token_model.hidden_dim)
    hidden_history = []
    tokens = []

    for t in range(max_tokens):
        prev_token = tokens[-1] if tokens else 0
        h_next, logits = token_model.step(prev_token, ret_ctx.state)
        ret_ctx.update(h_next)
        hidden_history.append(h_next)

        if (t + 1) % packet_size == 0:
            # mean without numpy
            aggregated = []
            for i in range(token_model.hidden_dim):
                s = sum(h[i] for h in hidden_history[-packet_size:])
                aggregated.append(s / packet_size)

            packet_state.update(aggregated_hidden=aggregated,
                                field_state=field_state)
            field_state.update(packet_state=packet_state,
                               instructions_vec=instructions_vec)
            logits = packet_state.bias_logits(logits)

        token_id = logits.index(max(logits))
        tokens.append(token_id)

    return tokens


if __name__ == "__main__":
    hidden_dim = 32
    vocab_size = 100

    token_model = TokenModel(vocab_size=vocab_size, hidden_dim=hidden_dim)
    packet_state = PacketState(dim=hidden_dim)
    field_state = TeleodynamicField(dim=hidden_dim)

    instructions_vec = [random.uniform(-1, 1) for _ in range(hidden_dim)]

    seq = generate(token_model, packet_state, field_state,
                   instructions_vec, max_tokens=40, packet_size=8)

    print("Generated token IDs:", seq)
