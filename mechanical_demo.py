"""
mechanical_demo.py — Juhász Model 1.0 physical demonstrator

This simulation models the actual mechanical core:
- two rotating discs (R1, R2) with 1:2 gear ratio
- a ball moving radially on disc R1
- collision at the center with disc R2
- impulse transfer and asymmetric, forward-moving state evolution
"""

import math

# -----------------------------
# Physical parameters
# -----------------------------
R1 = 2.0          # radius of disc 1
R2 = 1.0          # radius of disc 2 (1:2 ratio)
m_ball = 1.0      # mass of the ball
m_disc = 5.0      # effective mass of disc 2

omega1 = 0.5      # initial angular velocity of disc 1
omega2 = 0.0      # initial angular velocity of disc 2

phase_delay = 0.03        # damping factor per cycle

# -----------------------------
# Collision model
# -----------------------------
def collision_transfer(omega1):
    """
    Ball moves radially inward on disc R1.
    At the center, it collides with disc R2.
    The collision transfers angular momentum to disc 2.
    """
    v_ball = omega1 * R1
    p_ball = m_ball * v_ball

    delta_omega2 = p_ball / (m_disc * R2)
    return delta_omega2

# -----------------------------
# Hybrid mechanical update
# -----------------------------
def mechanical_update(omega1, omega2):
    # continuous dynamics on disc 1
    Fc = m_ball * (omega1 ** 2) * R1

    # collision → impulse transfer to disc 2
    delta_omega2 = collision_transfer(omega1)
    omega2 += delta_omega2

    # phase delay (damping)
    omega1 *= (1 - phase_delay)
    omega2 *= (1 - phase_delay)

    return omega1, omega2, Fc, delta_omega2

# -----------------------------
# Simulation loop
# -----------------------------
if __name__ == "__main__":
    print("Juhász Model 1.0 — Mechanical Demonstrator\n")
    print("cycle | omega1 | omega2 | Fc | impulse")
    print("---------------------------------------------")

    for cycle in range(1, 21):
        omega1, omega2, Fc, impulse = mechanical_update(omega1, omega2)
        print(f"{cycle:5d} | {omega1:.5f} | {omega2:.5f} | {Fc:.5f} | {impulse:.5f}")
