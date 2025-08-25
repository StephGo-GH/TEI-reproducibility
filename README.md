# Theory of Informational Emergence (TEI)

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/status-preprint-blue)

## Overview

The **Theory of Informational Emergence (TEI)** proposes that our observable Universe
(Post-Emergence) emerges from a more fundamental, timeless, spaceless, informational substrate
(Pre-Emergence).  

- **Pre-Emergence**: no space, no time, only a causal network of pure informational states.  
- **Post-Emergence**: space-time, matter, and physical laws appear as effective descriptions when
the substrate is updated step by step.  
- **Big Bang**: not a past explosion, but a *permanent front of emergence*, refreshed at each instant.  

This framework aims to unify gravitation, fundamental interactions, and cosmology through
rigorous mathematical tools (Γ-convergence) and falsifiable predictions.

---

## Paper / Preprint
- HAL: (à venir)
- arXiv: (à venir)

---

## Key Results

- **Mathematical Foundations**:  
  Γ-convergence proof from discrete causal graphs → continuous action (scalar-tensor + U(1) field).  
  Includes Poincaré inequality, compactness, and independence of discretization.

- **Gravity & PPN tests**:  
  Recovers Newtonian limit and General Relativity up to post-Newtonian parameters of order 2.  

- **Cosmology**:  
  Modified Friedmann equations with a scalar field *n(t)* unifying dark matter and dark energy.  
  Fits DESI DR2 + Euclid DR1 + Planck data with:  
  - H₀ = 67.55 ± 0.35 km/s/Mpc  
  - σ₈ = 0.809 ± 0.010  
  - w₀ = -0.87 ± 0.05  
  - wₐ = -0.41 ± 0.12  

- **Bridge with the Standard Model**:  
  Fermion masses and Yukawa couplings emerge from self-interaction with the substrate.  
  Predicts measurable deviations (Δy_f / y_f ≈ 0.5–1% for 2nd/3rd generation fermions).  

---

## Falsifiable Predictions

| Prediction | Observable/Test | Facility | Horizon |
|------------|-----------------|----------|----------|
| **P1**     | Quadratic photon dispersion (Δt ∝ E²) | LHAASO, CTA, Fermi | 2026 |
| **P2**     | Log-periodic oscillations in CMB power spectrum | CMB-S4, Simons Obs. | 2027 |
| **P3**     | Differential decoherence (Earth vs orbit) | ACES, Micius | 2028 |
| **P4**     | PPN 2nd order corrections (χ₁, χ₂) | Shapiro delay, pulsars | 2026–2030 |
| **P5**     | Yukawa coupling deviations (~0.5–1%) | HL-LHC, FCC | 2027–2040 |

---

## Repository Structure

```

tei\_github/
│
├── sim/                # Core simulation scripts
│   ├── graph\_generators.py
│   ├── poincare\_check.py
│   ├── gamma\_convergence.py
│   └── hyperbolicity\_test.py
│
├── tests/              # Pytest unit tests
├── data/               # Input/output datasets
├── figures/            # Generated figures
├── math/               # Notes & derivations
│
├── README.md           # This file
├── REPRODUCIBILITY.md  # How to reproduce results
├── environment.yml     # Conda environment
├── CITATION.cff        # Citation metadata
└── LICENSE             # MIT License

````

---

## Reproducibility

1. Install dependencies:
   ```bash
   conda env create -f environment.yml
   conda activate tei
   ````

2. Generate a random graph:

   ```bash
   python sim/graph_generators.py --dim 4 --N 50000 --seed 42 --out data/seeds/g_5e4_d4.npz
   ````

3. Check Poincaré inequality:

   ```bash
   python sim/poincare_check.py --graph data/seeds/g_5e4_d4.npz --samples 8 --out figures/fig_poincare_ratio.png
   ````

4. Test Γ-convergence:

   ```bash
   python sim/gamma_convergence.py --dim 4 --Ns 20000 40000 80000 --out figures/fig_action_convergence.png
   ````

5. Run unit tests:

   ```bash
   pytest -q
   ````
## Example result
After running:
```bash
python sim/graph_generators.py --dim 4 --N 20000 --seed 42 --out data/seeds/g_2e4_d4.npz
python sim/poincare_check.py --graph data/seeds/g_2e4_d4.npz --samples 4 --out figures/fig_poincare_ratio.png
   ````
---

## Citation

If you use this framework, please cite:

```bibtex
@misc{goulet2025tei,
  author       = {Stéphane Goulet},
  title        = {Theory of Informational Emergence (TEI) — Reproducibility Package},
  year         = {2025},
  url          = {https://github.com/StephGo-GH/tei-reproducibility},
  note         = {Preprint, under open review}
}
```

---

## License

This project is licensed under the MIT License.
