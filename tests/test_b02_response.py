# tests/test_b02_response.py
"""Task 4 small-case permanents (P5): spanning certificate and response identity at n = 4."""
from experiments.B02.response import check_signature, spanning_rank
from experiments.B02.run import hand_control


def test_kn_products_span():
    """Certificate control: rank mod p of the 55 KN products = 20 = dim at n = 4."""
    assert spanning_rank(4) == (20, 20)


def test_response_identity_small():
    """Test 5, scope: identity for (3,1) (spanning set x all branches)."""
    row = check_signature(3, 1)
    assert row == {"signature": [3, 1], "inputs": 55, "cases": 2640, "nonzero_outputs": 912}


def test_hand_control():
    """Independent nonzero control (KN(g, g), CCC, Phi1 = F)."""
    assert hand_control(3, 1)
