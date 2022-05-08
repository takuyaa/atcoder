from typical90.d import solve_d


def test_solve_d():
    assert solve_d(A=[[1, 1, 1], [1, 1, 1], [1, 1, 1]], H=3, W=3) == [
        [5, 5, 5],
        [5, 5, 5],
        [5, 5, 5],
    ]
    assert solve_d(A=[[3, 1, 4, 1], [5, 9, 2, 6], [5, 3, 5, 8], [9, 7, 9, 3]], H=4, W=4) == [
        [28, 28, 25, 26],
        [39, 33, 40, 34],
        [38, 38, 36, 31],
        [41, 41, 39, 43],
    ]