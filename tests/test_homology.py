import sympy as sp
from logicbound.homology import survivor_classes, projection_operator, LBIF

def test_projection_rank():
    vB, vL = survivor_classes(1, 2)
    pi = projection_operator(vB, vL)
    assert LBIF(pi) == 2