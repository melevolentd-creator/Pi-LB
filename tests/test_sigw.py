from logicbound.sigw import eta_L, R, OmegaGW

def test_eta_L():
    assert eta_L(1, 2, 3, 4) == 4 * 1 - 2 * 3

def test_R():
    assert R(2) == 4

def test_OmegaGW():
    assert OmegaGW(5) == 5