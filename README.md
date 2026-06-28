# Juhász Model — Hybrid Dynamics and Teleodynamic Demonstrators

This repository contains several minimal, fully transparent dynamical demonstrations illustrating core mechanisms of the Juhász Model (versions 1.0–12.0). Each module isolates one aspect of the unified scale‑field and teleodynamic framework, allowing the underlying behavior to be inspected, tested, and extended.

The demonstrations show how asymmetric, forward‑moving, non‑recurrent state evolution naturally emerges from hybrid update rules, delayed interactions, and teleodynamic field guidance. These mechanisms mirror the AGEINT cycle:

collapse → substitution → guidance.

---

## 🔹 1. Hybrid Update Demonstrator (Minimal Hybrid Rule)

This module illustrates the mechanical core of the Juhász Model:  
**continuous Fc‑dynamics combined with discrete packet updates**.

- Continuous force:  
  `Fc = m · ω² · r`
- Discrete packet update:  
  `ω → ω + impulse`
- Phase delay produces asymmetric, non‑recurrent evolution.

Because each packet update shifts the state forward, the trajectory becomes **spiral‑like**, converging toward a stable attractor without ever returning to a previous state.

This hybrid mechanism is the computational analogue of the Juhász Model’s collapse → substitution → guidance cycle.

### Highlights
- Hybrid state updates  
- Packet‑based dynamics  
- Phase‑delay behavior  
- Spiral attractor geometry  
- Non‑recurrent state evolution

---

## 🔹 2. Mechanical Demonstrator (Juhász Model 1.0)

A physical simulation of the two‑disk mechanical core:

- Radii R1 and R2 (1:2 ratio)  
- A sphere moving radially on R1  
- Collision at the center with R2  
- Impulse transfer  
- Asymmetric forward‑shifted state evolution  
- Spiral‑like attractor behavior

This model shows how the same asymmetric, non‑recurrent state chain emerges in a real mechanical configuration.

---

## 🔹 3. Proton–Electron Delayed Interaction Demonstrator

This module extends the asymmetric forward‑moving dynamics into the electromagnetic domain.  
It simulates proton–electron interaction under:

- Coulomb force  
- Lorentz magnetic force  
- Small gravitational attraction  
- **Retarded position** due to finite propagation speed:

r_ret = r(t - |r| / c)


Neither particle reacts to the other’s instantaneous position.  
Each reacts to where the other **was**, producing characteristic lag behavior.

The faster electron accelerates toward the proton’s *past* position, not its present one.  
This velocity‑dependent asymmetry generates:

- forward‑moving, non‑recurrent evolution  
- spiral‑like stabilization  
- no collapse  
- no closed orbit

This demonstrates how hybrid, forward‑moving state chains naturally arise even in classical two‑body systems when finite propagation speed is included.

---

## 🔹 4. Teleodynamic Steering Demonstrator

A second, independent module showing how teleodynamic principles apply to generative systems.

A **packet‑level steering layer** is placed above a dummy generative model:

1. **Packet‑State**  
   Short‑range memory accumulating hidden activity over 8‑token windows.

2. **Field‑State**  
   A slowly evolving teleodynamic field influenced by packet‑state and a fixed instruction vector.  
   Over time, the field becomes a **directional attractor**.

3. **Logit‑Bias Feedback**  
   The field feeds back into the logits using a tanh‑like bias.  
   Even a small bias produces **measurable directional drift** in token selection.

The demo runs for 40 steps and prints ASCII heatmaps of packet‑state and field‑state evolution.

### Drift Measurement
The system computes:

- mean token ID per packet  
- variance per packet  

Random systems fluctuate.  
Teleodynamic steering produces:

- stable drift toward a preferred region  
- decreasing variance  
- structured field‑state evolution

This is a minimal computational analogue of teleodynamic guidance in the Juhász Model 12.0.

---

## 🔹 Future Extensions

Planned modules include:

- Teleonomic field interactions  
- Teleodynamic control  
- Attractor visualization  
- Full hybrid simulation  
- AGEINT‑compatible analysis tools

---

## 🔹 Zenodo References (DOI)

These demonstrations are based on the published Juhász Model papers:

- Juhász Model 1.0 — https://doi.org/10.5281/zenodo.20776920  
- Juhász Model 3.0 — https://doi.org/10.5281/zenodo.20270739  
- Juhász Model 4.1 — https://doi.org/10.5281/zenodo.20347018  
- Juhász Model 8.0 — https://doi.org/10.5281/zenodo.20674998  
- Juhász Model 9.0 — https://doi.org/10.5281/zenodo.20675094  
- Juhász Model 10.0 — https://doi.org/10.5281/zenodo.20675287  
- Juhász Model 11.0 — https://doi.org/10.5281/zenodo.20675388  
- Juhász Model 12.0 — https://doi.org/10.5281/zenodo.20675497  

---

## 🔹 Version

First public multi‑module demonstrator — Juhász Model Demo
