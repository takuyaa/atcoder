from abc251.a import solve_a


def test_solve_a():
    assert solve_a("abc") == "abcabc"
    assert solve_a("zz") == "zzzzzz"
