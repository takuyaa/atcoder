from typical90.l import solve_l


def test_solve_l():
    list(
        solve_l(
            H=3,
            W=3,
            queries=[
                "1 2 2",
                "1 1 1",
                "2 1 1 2 2",
                "1 3 2",
                "2 1 1 2 2",
                "2 2 2 3 2",
                "1 2 3",
                "1 2 1",
                "2 1 1 2 2",
                "2 1 1 3 3",
            ],
        )
    ) == [
        "No",
        "No",
        "Yes",
        "Yes",
        "No",
    ]
