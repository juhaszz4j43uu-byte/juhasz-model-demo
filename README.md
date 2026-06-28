Juhász Model — Hybrid Dynamics Demonstrator
This repository contains a minimal, transparent demonstration of the hybrid update rule
that forms the mechanical core of the Juhász Model. The example illustrates how
continuous dynamics (Fc = m·ω²·r) combine with discrete packet updates
(ω → ω + impulse) and phase delay to produce asymmetric, non‑recurrent
state evolution.

🔹 Core Concept
The system never returns to a previous state.
Each cycle computes a continuous force value, then applies a discrete packet update.
Because every update shifts the state forward, the trajectory becomes a spiral‑like
progression toward a stable attractor.

This hybrid mechanism mirrors AGEINT’s internal logic:

collapse → packet boundary

substitution → ω updated by impulse

guidance → convergence toward an attractor

🔹 Why This Demonstrator Matters
This project provides a computational entry point for understanding the deeper
structure of the Juhász Model. It isolates the hybrid update rule so that the core
behavior is easy to inspect, test, and extend.

It highlights:

hybrid state updates

packet‑based dynamics

phase‑delay behavior

spiral‑attractor geometry

non‑recurrent state evolution

This mechanical core is only an analogy for the hybrid update rule.
The full Juhász Model (3.0–12.0) is a unified scale‑field and teleodynamic framework
that extends far beyond the mechanical demonstrator.

🔹 Mechanical Demonstrator (physical model)
The repository also includes a physical simulation of the Juhász Model 1.0
mechanical core (mechanical_demo.py). This model implements the actual
two‑disc system with:

R1 and R2 radii (1:2 gear ratio)

a ball moving radially on disc R1

collision at the center with disc R2

impulse transfer and asymmetric state evolution

forward‑moving spiral‑like attractor behavior

This physical demonstrator complements the minimal hybrid update example by
showing how the same asymmetric, non‑recurrent state chain emerges from a
real mechanical configuration.

🔹 Proton–Electron Retarded Interaction Demonstrator
This demonstrator extends the asymmetric, forward‑moving dynamics of the Juhász Model
into the electromagnetic domain. It simulates a proton and an electron interacting
under multiple classical forces while incorporating retarded electromagnetic interaction —
meaning that neither particle responds to the other’s instantaneous position.
Instead, each particle reacts to the other’s past position, shifted by the finite
propagation speed of electromagnetic influence:

r_ret = r(t - |r|/c)

This delay produces the characteristic falling‑behind behavior:
the faster electron does not accelerate toward the proton’s current location,
but toward where the proton used to be. This velocity‑dependent asymmetry
generates a forward‑moving, non‑recurrent state evolution and a spiral‑like approach
rather than a simple collapse or closed orbit.

The simulation includes:

Coulomb force between proton and electron

Lorentz magnetic force from velocity × magnetic field

tiny gravitational attraction (included for completeness)

retarded position calculation based on finite signal speed

asymmetric trajectory caused by velocity‑dependent delay

spiral‑like stabilization instead of circular or collapsing motion

This demonstrator complements the mechanical model by showing how the Juhász Model’s
asymmetric, non‑recurrent dynamics naturally emerge in a real physical system when
finite propagation speed is taken into account. It illustrates how hybrid,
forward‑moving state chains arise even in classical two‑body interactions once
retardation is included.

🔹 Future Extensions
Planned modules include:

teleonomic field interaction

teleodynamic guidance

attractor visualization

full hybrid simulation

AGEINT‑compatible analysis tools

🔹 References (Zenodo DOIs)
This demonstrator is based on the published Juhász Model papers:

Juhász Model 1.0 — https://doi.org/10.5281/zenodo.20776920

Juhász Model 3.0 — https://doi.org/10.5281/zenodo.20270739

Juhász Model 4.1 — https://doi.org/10.5281/zenodo.20347018

Juhász Model 8.0 — https://doi.org/10.5281/zenodo.20674998

Juhász Model 9.0 — https://doi.org/10.5281/zenodo.20675094

Juhász Model 10.0 — https://doi.org/10.5281/zenodo.20675287

Juhász Model 11.0 — https://doi.org/10.5281/zenodo.20675388

Juhász Model 12.0 — https://doi.org/10.5281/zenodo.20675497

🔹 Version
Initial public demonstrator — Juhász Model Demo
