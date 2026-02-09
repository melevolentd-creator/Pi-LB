# Logic-Bound Framework

**Homological Invariants and Scalar-Induced Gravitational Wave (SIGW) Predictions**

A research-grade Python framework implementing homological and information-theoretic approaches to baryogenesis and gravitational wave physics.

---

## Overview

The Logic-Bound framework provides computational tools for:

1. **Homological Analysis** — Differential complexes, survivor classes, and Logic-Bound Invariant Factors (LBIF)
2. **Parameter Sampling** — Constrained slice sampling for physical parameter exploration
3. **SIGW Physics** — Gravitational wave spectral predictions from fundamental parameters
4. **Visualization** — Publication-quality plotting for papers and presentations
5. **Bayesian Inference** — MCMC-ready likelihood computations

---

## Installation

### From Source

```bash
git clone https://github.com/melevolentd-creator/Pi-LB.git
cd Pi-LB
pip install -e .
```

### Requirements

- Python ≥ 3.9
- numpy
- sympy
- matplotlib
- scipy
- emcee

---

## Quick Start

### Basic Usage

```python
import numpy as np
from logicbound import homology, sampling, sigw, plotting

# Define parameter ranges
epsilon_range = np.linspace(0.1, 0.9, 100)
kappa_range = np.linspace(0.01, 0.1, 100)

# Sample the Logic-Bound slice
points = sampling.sample_slice(
    epsilon_range, kappa_range,
    eta_b_obs=1e-10, c_sph=1e-12
)

# Compute SIGW spectrum for a sample point
if points:
    eps1, kap1, eps2, kap2 = points[0]
    eta = sigw.eta_L(eps1, kap1, eps2, kap2)
    R = sigw.R(eta, alpha=1.0)
    
    # Generate frequency array and spectrum
    fvals = np.logspace(-3, 0, 100)
    Omega_vals = sigw.spectrum(R, fvals, beta=1.0)
    
    # Plot
    fig = plotting.plot_spectrum(fvals, Omega_vals)
    fig.savefig("spectrum.pdf")
```

### Homological Analysis

```python
from logicbound import homology

# Define symbolic parameters
eps1, eps2, kap1, kap2, Gamma = homology.differential_symbols()[:5]

# Compute survivor classes
vB, vL = homology.survivor_classes(kap1, kap2)

# Project onto survivor subspace
P = homology.projection_operator(vB, vL)
```

---

## Project Structure

```
logicbound/
├── homology.py       # Differential complexes and invariants
├── sampling.py       # Logic-Bound slice sampling
├── sigw.py          # SIGW physics and spectra
├── plotting.py      # Publication-quality figures
├── inference.py     # Bayesian inference skeleton
├── utils.py         # Shared utilities
└── __init__.py

tests/
├── test_homology.py
├── test_sampling.py
└── test_sigw.py
```

---

## Core Modules

### `homology.py`

Implements the homological framework:
- Differential symbols and complexes
- Survivor classes (baryon-number, lepton-number)
- Projection operators onto survivor subspaces
- Logic-Bound Invariant Factor (LBIF) computation

### `sampling.py`

Constrained parameter sampling:
- `solve_kap2()` — Solve for kappa₂ from other constraints
- `sample_slice()` — Generate valid parameter points

### `sigw.py`

Gravitational wave physics:
- `eta_L()` — Fundamental baryon asymmetry parameter
- `R()` — Normalized asymmetry-squared
- `OmegaGW()` — Gravitational wave energy density
- `transfer_function()` — Frequency-dependent amplitude modulation
- `spectrum()` — Full frequency-dependent spectrum

### `plotting.py`

Figure generation (publication-ready):
- `plot_prediction_band()` — R vs Ω_GW scatter plot
- `plot_spectrum()` — Frequency-dependent spectrum
- `plot_detector_overlay()` — Spectrum vs detector sensitivity

### `inference.py`

MCMC likelihood:
- `log_likelihood()` — Full probability model for parameter estimation

---

## Example: Full Pipeline

See `notebooks/logicbound_notebook.ipynb` for a complete walkthrough of:
1. Parameter space sampling
2. SIGW spectrum computation
3. Detector overlap analysis
4. Visualization for papers

---

## Testing

Run the full test suite:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov=logicbound
```

---

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

Key contribution areas:
- Numerical stability improvements
- Additional transfer function models
- Extended MCMC sampling
- Documentation and examples

---

## Citation

If you use this framework in your research, please cite:

```bibtex
@software{logic_bound_2026,
  author = {Danny},
  title = {Logic-Bound Framework: Homological Invariants and SIGW Predictions},
  year = {2026},
  url = {https://github.com/melevolentd-creator/Pi-LB}
}
```

To obtain a persistent DOI, see [Zenodo Integration](#zenodo).

---

## Zenodo Integration

To enable DOI assignment and academic citations:

1. Push to GitHub and make the repository public
2. Sign in at [Zenodo](https://zenodo.org/)
3. Connect your GitHub account
4. Enable the Pi-LB repository
5. Create a release on GitHub — Zenodo automatically mints a DOI

---

## License

MIT License. See [LICENSE](LICENSE) for details.

---

## References

- Core framework papers and preprints (add links)
- Related SIGW literature
- Homological algebra references

---

## Questions or Issues?

Open an issue on GitHub: https://github.com/melevolentd-creator/Pi-LB/issues

For discussions and announcements, enable [GitHub Discussions](https://github.com/melevolentd-creator/Pi-LB/discussions).