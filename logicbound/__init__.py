"""
Logic-Bound Framework: Homological Invariants and SIGW Predictions

A research package implementing homological and information-theoretic
approaches to baryogenesis and scalar-induced gravitational waves (SIGWs).
"""

__version__ = "0.1.0"
__author__ = "Danny"

from . import homology
from . import sampling
from . import sigw
from . import plotting
from . import inference
from . import utils

__all__ = [
    "homology",
    "sampling",
    "sigw",
    "plotting",
    "inference",
    "utils",
]