from typical90.p import solve_p


def test_solve_p():
    assert solve_p(N=227, A=21, B=47, C=56) == 5
    assert solve_p(N=9999, A=1, B=5, C=10) == 1004
    assert solve_p(N=998244353, A=314159, B=265358, C=979321) == 3333
