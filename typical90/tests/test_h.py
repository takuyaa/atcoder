from typical90.h import solve_h


def test_solve_h():
    assert solve_h("attcordeer") == 4
    assert solve_h("xattcordeerzz") == 4
    assert solve_h("btwogablwetwoiehocghiewobadegwhoihegnldir") == 2
    assert (
        solve_h(
            "aaaaaaaaaaaaaaaaaaaattttttttttttttttttttccccccccccccccccccccooooooooooooooooooooddddddddddddddddddddeeeeeeeeeeeeeeeeeeeerrrrrrrrrrrrrrrrrrrr"  # noqa: E501
        )
        == 279999993
    )
