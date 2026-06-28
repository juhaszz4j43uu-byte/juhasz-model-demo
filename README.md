# Juhász Model — Hybrid Dynamics Demonstrator

This repository contains a minimal demonstration of the hybrid update rule that forms
the core behavior of the Juhász Model. The demonstrator shows how continuous dynamics
(**Fc = m·ω²·r**) combine with discrete packet updates (**ω → ω + impulse**) and phase
delay to produce asymmetric, non‑recurrent state evolution.

---

## 🔹 Core Concept

The system **never returns to a previous state**.  
Each cycle computes a continuous force value, then applies a discrete packet update.
Because every update shifts the system forward, the trajectory becomes a spiral‑like
progression toward a stable attractor.

This hybrid mechanism mirrors AGEINT’s internal logic:

- **collapse** → discrete packet boundary  
- **substitution** → ω updated by impulse  
- **guidance** → convergence toward an attractor  

---

## 🔹 Why This Demonstrator Matters

This project provides a computational entry point for understanding:

- hybrid state updates  
- packet‑based dynamics  
- phase delay behavior  
- spiral attractor geometry  
- non‑recurrent state evolution  

It is intentionally minimal so that the update rule is clear and easy to extend.

---

## 🔹 Future Extensions

Additional modules will be added:

- teleonomic field interaction  
- teleodynamic guidance  
- attractor visualization  
- full hybrid simulation  
- AGEINT‑compatible analysis tools

---

## 🔹 References (Zenodo DOIs)

This demonstrator is based on the published Juhász Model papers:

- **Juhász Model 1.0** — https://doi.org/10.5281/zenodo.20776920  
- **Juhász Model 3.0** — https://doi.org/10.5281/zenodo.20270739  
- **Juhász Model 4.1** — https://doi.org/10.5281/zenodo.20347018  
- **Juhász Model 8.0** — https://doi.org/10.5281/zenodo.20674998  
- **Juhász Model 9.0** — https://doi.org/10.5281/zenodo.20675094  
- **Juhász Model 10.0** — https://doi.org/10.5281/zenodo.20675287  
- **Juhász Model 11.0** — https://doi.org/10.5281/zenodo.20675388  
- **Juhász Model 12.0** — https://doi.org/10.5281/zenodo.20675497  

---

## 🔹 Version

**Initial public demonstrator — Juhász Model Demo**
