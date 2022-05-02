from typical90.a import can_devide, solve_a


def test_solve_a():
    assert solve_a(N=3, L=34, K=1, A=[8, 13, 26]) == 13
    assert solve_a(N=7, L=45, K=2, A=[7, 11, 16, 20, 28, 34, 38]) == 12
    assert solve_a(N=3, L=100, K=1, A=[28, 54, 81]) == 46
    assert solve_a(N=3, L=100, K=2, A=[28, 54, 81]) == 26
    assert (
        solve_a(
            N=20,
            L=1000,
            K=4,
            A=[51, 69, 102, 127, 233, 295, 350, 388, 417, 466, 469, 523, 553, 587, 720, 739, 801, 855, 926, 954],
        )
        == 170
    )


def test_can_devide():
    assert can_devide(A=[8, 13, 26], K=1, L=34, min_length=17) is False
    assert can_devide(A=[8, 13, 26], K=1, L=34, min_length=12) is True
