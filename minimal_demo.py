This script implements a minimal hybrid update cycle for the Juhász Model 1.0:
- mechanical core (Fc = m * omega**2 * r)
- Planck-like energy packets (discrete impulses on omega)
- asymmetric state formation (the system never returns to a previous state)

All forces, laws, and interactions are applied in a domain-specific way:
the update rules are always evaluated relative to the local scale, packet
structure, and interaction region.

This demonstrator is intentionally simple: it shows how continuous dynamics
combine with discrete packet updates to produce a forward-moving, asymmetric
state chain that converges toward a spiral-like attractor.
"""

import math

# -----------------------------
# Parameters (domain-specific)
# -----------------------------
m = 1.0          # mass (local domain value)
r = 1.0          # radius (local domain geometry)
omega = 0.5      # initial angular velocity
packet_impulse = 0.12   # Planck-like discrete impulse
phase_delay = 0.03      # small delay factor per cycle

# -----------------------------
# Hybrid update rule
# -----------------------------
def hybrid_update(omega):
    """
    One hybrid update cycle:
    1. Continuous force computation (Fc = m * omega^2 * r)
    2. Discrete packet update (omega += impulse)
    3. Phase delay (omega *= (1 - delay))
    """
    Fc = m * (omega ** 2) * r
    omega += packet_impulse
    omega *= (1 - phase_delay)
    return omega, Fc

# -----------------------------
# Demonstration loop
# -----------------------------
if __name__ == "__main__":
    print("Juhász Model 1.0 — Hybrid Update Demonstrator\n")
    print("cycle | omega | Fc")
    print("----------------------")

    for cycle in range(1, 21):
        omega, Fc = hybrid_update(omega)
        print(f"{cycle:5d} | {omega:.5f} | {Fc:.5f}")
