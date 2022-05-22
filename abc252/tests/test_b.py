from abc252.b import solve_b


def test_solve_b():
    assert solve_b(A=[6, 8, 10, 7, 10], B=[2, 3, 4])
    assert not solve_b(A=[100, 100, 100, 1, 1], B=[5, 4])
    assert not solve_b(A=[100, 1], B=[2])
