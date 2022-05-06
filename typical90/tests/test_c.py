from typical90.c import solve_c


def test_solve_c():
    assert (
        solve_c(
            {
                1: {2},
                2: {1, 3},
                3: {2},
            }
        )
        == 3
    )
    assert (
        solve_c(
            {
                1: {2},
                2: {1, 3},
                3: {2, 4, 5},
                4: {3},
                5: {3},
            }
        )
        == 4
    )
