from typical90.f import solve_f


def test_solve_f():
    assert solve_f(7, 3, "atcoder") == "acd"
    assert solve_f(14, 5, "kittyonyourlap") == "inlap"

    assert solve_f(3, 3, "aaa") == "aaa"
    assert solve_f(5, 3, "aaaaa") == "aaa"
    assert solve_f(5, 3, "abcde") == "abc"
    assert solve_f(5, 3, "edcba") == "cba"

    assert solve_f(7, 3, "abcdabc") == "aab"
