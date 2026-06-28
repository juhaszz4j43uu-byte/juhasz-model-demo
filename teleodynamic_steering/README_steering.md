
# Teleodynamic Steering Demonstrator
A minimal, runnable example of packet-level state updates, teleodynamic field evolution, and logit-bias feedback applied to a generative system.

## Overview

This module implements a teleodynamic steering layer that can be placed on top of any generative model. The goal is to demonstrate how a slowly evolving teleodynamic field can bias token-level dynamics, producing directional drift even when the underlying model is completely random.

The mechanism mirrors the Juhász Model’s collapse → substitution → guidance cycle, applied here to token generation rather than physical state evolution.

This demonstrator is intentionally minimal and dependency-free, so that the dynamics remain fully visible.

---

## Key Components

### 1. Packet-State (medium-range memory)
Aggregates hidden activity over short windows (8 tokens). Acts as a bridge between token-level fluctuations and long-range field evolution.

### 2. Field-State (long-range attractor)
A slowly evolving teleodynamic field that incorporates:
- packet-state contributions
- a fixed instruction vector (goal direction)

Over time, the field becomes a directional attractor.

### 3. Logit-Bias Feedback
The field feeds back into the generative process by adding a small bias to the logits. This bias is computed using a tanh-like function of the field’s mean value.

Even a small bias, applied consistently, produces non-random drift in token selection.

---

## How the Demo Works

The demo runs for 40 steps using a dummy LLM:
- hidden states are random
- logits are random
- the steering layer updates packet-state every step
- every 8 steps, it updates the field and biases the logits
- the next token is chosen as argmax(logits)

Despite the randomness, the token sequence begins to cluster in a preferred region of the vocabulary. This is the teleodynamic steering effect.

ASCII heatmaps show the evolution of packet-state and field-state after each packet.

---

## Drift Measurement

To quantify directional drift, the demo computes:
- mean token ID per packet
- variance per packet

If the system were purely random:
- packet means would fluctuate around the center
- variance would remain high

With teleodynamic steering:
- packet means begin to shift toward a stable region
- variance often decreases, indicating convergence
- the field-state becomes progressively structured

This provides a clear, numerical demonstration of teleodynamic influence.

---

## Files

- teleodynamic_steering.py  
  Core steering module (packet-state, field-state, logit-bias).

- teleodynamic_steering_demo.py  
  40-step runnable demonstration with heatmaps and drift measurement.

- README_steering.md  
  This document.

---

## How to Run

