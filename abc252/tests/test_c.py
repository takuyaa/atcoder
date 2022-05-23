from abc252.c import solve_c


def test_solve_c():
    assert (
        solve_c(
            S=[
                "1937458062",
                "8124690357",
                "2385760149",
            ]
        )
        == 6
    )
    assert (
        solve_c(
            S=[
                "0123456789",
                "0123456789",
                "0123456789",
                "0123456789",
                "0123456789",
            ]
        )
        == 40
    )
