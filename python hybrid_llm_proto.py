# hybrid_llm_proto.py
import np


class TokenModel:
    def __init__(self, vocab_size=100, hidden_dim=32):
        self.vocab_size = vocab_size
        self.hidden_dim = hidden_dim

    def step(self, token_id, context_state):
        """
        Stub token-lépés: visszaad egy hidden state-et és logitvektort.
        Itt nincs valódi nyelvi modell, csak zaj, hogy lássuk a dinamikát.
        """
        h_next = np.random.randn(self.hidden_dim)
        logits = np.random.randn(self.vocab_size)
        return h_next, logits


class PacketState:
    def __init__(self, dim):
        self.vec = np.zeros(dim)

    def update(self, aggregated_hidden, field_state):
        """
        Diszkrét csomagfrissítés: S_{k+1} = S_k + ΔS(h_agg, F_k)
        """
        delta = 0.1 * aggregated_hidden + 0.05 * field_state.vec
        self.vec = self.vec + delta
        return self.vec

    def bias_logits(self, logits):
        """
        Guidance: packet-állapotból egy skalár bias a logitokra.
        Nem szép, de jól mutatja a hibrid hatást.
        """
        scale = np.tanh(self.vec.mean())
        return logits + scale


class TeleodynamicField:
    def __init__(self, dim):
        self.vec = np.zeros(dim)

    def update(self, packet_state, instructions_vec):
        """
        Lassú teleodinamikus mező: F_{k+1} = F_k + G(S_k, I)
        I: instrukciók / feladat vektora.
        """
        delta = 0.01 * packet_state.vec + 0.1 * instructions_vec
        self.vec = self.vec + delta
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
            return np.zeros(self.hidden_dim)
        # retardált, simított múlt-kontekstus
        return np.mean(self.buffer, axis=0)


def generate(token_model, packet_state, field_state,
             instructions_vec, max_tokens=40, packet_size=8):
    """
    Fő hibrid loop:
    - token-szintű lépések retardált kontextussal
    - csomaghatáron S_k és F_k frissítés
    - guidance: packet-bias a logitokra
    """
    ret_ctx = RetardedContext(hidden_dim=token_model.hidden_dim)
    hidden_history = []
    tokens = []

    for t in range(max_tokens):
        # 1) token-lépés retardált kontextussal
        prev_token = tokens[-1] if tokens else 0
        h_next, logits = token_model.step(prev_token, ret_ctx.state)
        ret_ctx.update(h_next)
        hidden_history.append(h_next)

        # 2) csomaghatár: hibrid frissítés
        if (t + 1) % packet_size == 0:
            aggregated = np.mean(hidden_history[-packet_size:], axis=0)
            packet_state.update(aggregated_hidden=aggregated,
                                field_state=field_state)
            field_state.update(packet_state=packet_state,
                               instructions_vec=instructions_vec)
            logits = packet_state.bias_logits(logits)

        # 3) token kiválasztása
        token_id = int(np.argmax(logits))
        tokens.append(token_id)

    return tokens


if __name__ == "__main__":
    hidden_dim = 32
    vocab_size = 100

    token_model = TokenModel(vocab_size=vocab_size, hidden_dim=hidden_dim)
    packet_state = PacketState(dim=hidden_dim)
    field_state = TeleodynamicField(dim=hidden_dim)

    # „system prompt” / instrukciók vektora
    instructions_vec = np.random.randn(hidden_dim)

    seq = generate(token_model, packet_state, field_state,
                   instructions_vec, max_tokens=40, packet_size=8)

    print("Generated token IDs:", seq)
