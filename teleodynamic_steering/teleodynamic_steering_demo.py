# teleodynamic_steering_demo.py
import random


class TeleodynamicSteeringLayer:
    """
    Teleodinamikus steering modul:
    - packetenként frissíti a mezőt
    - a mező visszahat a logitokra
    - bármely LLM fölé rátehető
    """

    def __init__(self, dim=32, packet_size=8, field_gain=0.1, packet_gain=0.05):
        self.dim = dim
        self.packet_size = packet_size

        # packet-state (középtávú állapot)
        self.packet_state = [0.0] * dim

        # teleodinamikus mező (hosszútávú célmező)
        self.field_state = [0.0] * dim

        # instructions (irányvektor)
        self.instructions_vec = [random.uniform(-1, 1) for _ in range(dim)]

        self.field_gain = field_gain
        self.packet_gain = packet_gain

        self.t = 0  # token counter

    def _update_packet_state(self, hidden_vec):
        new_vec = []
        for h, f, p in zip(hidden_vec, self.field_state, self.packet_state):
            new_vec.append(p + self.packet_gain * h + 0.01 * f)
        self.packet_state = new_vec

    def _update_field_state(self):
        new_vec = []
        for p, instr, f in zip(self.packet_state, self.instructions_vec, self.field_state):
            new_vec.append(f + 0.01 * p + self.field_gain * instr)
        self.field_state = new_vec

    def _bias_logits(self, logits):
        mean_field = sum(self.field_state) / len(self.field_state)
        scale = (2 / (1 + pow(2.71828, -2 * mean_field))) - 1  # tanh approx
        return [x + scale for x in logits]

    def step(self, logits, hidden_vec):
        """
        Egy LLM-lépés:
        - kapjuk az LLM logitjait és hidden-állapotát
        - frissítjük a packetet / mezőt, ha packet-határhoz értünk
        - visszatorzítjuk a logitokat (teleodinamikus bias)
        """
        self.t += 1

        self._update_packet_state(hidden_vec)

        if self.t % self.packet_size == 0:
            self._update_field_state()
            logits = self._bias_logits(logits)

        return logits


class DummyLLM:
    """
    Egyszerű LLM-szimuláció:
    - random hidden
    - random logits
    - a steering layer torzítja a logitokat
    """

    def __init__(self, vocab_size=100, hidden_dim=32):
        self.vocab_size = vocab_size
        self.hidden_dim = hidden_dim

    def step(self, prev_token_id):
        hidden = [random.uniform(-1, 1) for _ in range(self.hidden_dim)]
        logits = [random.uniform(-1, 1) for _ in range(self.vocab_size)]
        return hidden, logits


def ascii_bar(value):
    v = max(-1, min(1, value))
    length = int((v + 1) * 10)
    return "#" * length


def heat_row(vec):
    palette = " .:-=+*#%@"
    out = ""
    for v in vec:
        v = max(-1.0, min(1.0, v))
        s = (v + 1.0) / 2.0
        level = int(s * 10)
        out += palette[level]
    return out


if __name__ == "__main__":
    vocab_size = 100
    hidden_dim = 32

    llm = DummyLLM(vocab_size=vocab_size, hidden_dim=hidden_dim)
    steering = TeleodynamicSteeringLayer(dim=hidden_dim, packet_size=8)

    tokens = []

    print("\n=== TELEODYNAMIC STEERING DEMO (40 lépés) ===\n")

    for t in range(40):
        prev = tokens[-1] if tokens else 0
        hidden, logits = llm.step(prev)

        steered_logits = steering.step(logits, hidden)

        token_id = steered_logits.index(max(steered_logits))
        tokens.append(token_id)

        print(f"{t:02d}: token={token_id}")

        if (t + 1) % steering.packet_size == 0:
            print("\nPacket-State heatmap:")
            print(heat_row(steering.packet_state))

            print("Field-State heatmap:")
            print(heat_row(steering.field_state))
            print()

    print("\nFinal steered token sequence:")
    print(tokens)
