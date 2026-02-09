import sympy as sp
from logicbound.homology import survivor_classes, projection_operator

def test_projection_idempotent():
    vB, vL = survivor_classes(1, 2)
    pi = projection_operator(vB, vL)
    assert (pi * pi - pi).applyfunc(sp.simplify) == sp.zeros(5)