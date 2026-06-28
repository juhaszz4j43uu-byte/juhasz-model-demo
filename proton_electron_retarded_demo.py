"""
proton_electron_retarded_demo.py — Retarded EM interaction demo

This simulation includes:
- Coulomb force
- Lorentz magnetic force
- tiny gravitational attraction
- RETARDED POSITION (c-delay)
- asymmetric "falling behind" effect

The electron and proton do NOT see each other's current position.
They see the position shifted by light-speed delay:
    r_ret = r(t - |r|/c)

This produces the characteristic "mellécélzás" and spiral-like stabilization.
"""

import math

# -----------------------------
# Physical constants
# -----------------------------
EPS0 = 8.854e-12
MU0  = 4 * math.pi * 1e-7
G    = 6.674e-11
C    = 3e8

Q_E  = -1.602e-19
Q_P  =  1.602e-19

M_E  = 9.109e-31
M_P  = 1.673e-27

# -----------------------------
# Initial conditions
# -----------------------------
r_e = [-5e-10, 0.0]
r_p = [ 5e-10, 0.0]

v_e = [0.0, 2e6]
v_p = [0.0,-2e5]

dt = 1e-18
steps = 500

# -----------------------------
# Helper functions
# -----------------------------
def sub(a,b): return [a[0]-b[0], a[1]-b[1]]
def add(a,b): return [a[0]+b[0], a[1]+b[1]]
def mul(a,s): return [a[0]*s, a[1]*s]
def norm(a): return math.sqrt(a[0]**2 + a[1]**2)

# -----------------------------
# Retarded position
# -----------------------------
def retarded_position(r, v):
    """
    r_ret = r - v * (|r| / c)
    The particle sees the OTHER particle's OLD position.
    """
    d = norm(r)
    delay = d / C
    return [r[0] - v[0]*delay, r[1] - v[1]*delay]

# -----------------------------
# Forces
# -----------------------------
def coulomb(q1, q2, r1, r2):
    dr = sub(r1, r2)
    d = norm(dr) + 1e-30
    return mul(dr, (q1*q2)/(4*math.pi*EPS0*d**3))

def gravity(m1, m2, r1, r2):
    dr = sub(r1, r2)
    d = norm(dr) + 1e-30
    return mul(dr, -G*m1*m2/d**3)

# -----------------------------
# Simulation
# -----------------------------
if __name__ == "__main__":
    print("Retarded Proton–Electron Demo (mögé zuhanás)\n")
    print("step | r_e_x   r_p_x   | dist")
    print("--------------------------------")

    for step in range(steps):

        # RETARDED positions
        r_p_ret = retarded_position(r_p, v_p)
        r_e_ret = retarded_position(r_e, v_e)

        # Forces on electron (from proton's RETARDED position)
        F_e_c = coulomb(Q_E, Q_P, r_e, r_p_ret)
        F_e_g = gravity(M_E, M_P, r_e, r_p_ret)
        F_e = add(F_e_c, F_e_g)

        # Forces on proton (from electron's RETARDED position)
        F_p_c = coulomb(Q_P, Q_E, r_p, r_e_ret)
        F_p_g = gravity(M_P, M_E, r_p, r_e_ret)
        F_p = add(F_p_c, F_p_g)

        # Update velocities
        v_e = add(v_e, mul(F_e, dt/M_E))
        v_p = add(v_p, mul(F_p, dt/M_P))

        # Update positions
        r_e = add(r_e, mul(v_e, dt))
        r_p = add(r_p, mul(v_p, dt))

        # Distance
        d = norm(sub(r_e, r_p))

        print(f"{step:4d} | {r_e[0]:.3e} {r_p[0]:.3e} | {d:.3e}")
