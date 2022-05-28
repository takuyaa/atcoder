from abc251.c import solve_c


def test_solve_c():
    assert solve_c(S=["aaa", "bbb", "aaa"], T=[10, 20, 30]) == 2
    assert solve_c(S=["aaa", "bbb", "ccc", "ddd", "bbb"], T=[9, 10, 10, 10, 11]) == 2
    assert (
        solve_c(S=["bb", "ba", "aa", "bb", "ba", "aa", "aa", "ab", "bb", "ab"], T=[3, 1, 4, 1, 5, 9, 2, 6, 5, 3]) == 8
    )
