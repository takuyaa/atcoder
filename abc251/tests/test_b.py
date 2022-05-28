from abc251.b import solve_b


def test_solve_b():
    assert solve_b(A=[1, 3], W=10) == 3
    assert solve_b(A=[2, 3], W=1) == 0
    assert solve_b(A=[3, 3, 3, 3], W=12) == 3
    assert solve_b(A=[202, 20, 5, 1, 4, 2, 100], W=251) == 48
