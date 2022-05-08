from typical90.f import RMQ, solve_f


def test_solve_f():
    assert solve_f(7, 3, "atcoder") == "acd"
    assert solve_f(14, 5, "kittyonyourlap") == "inlap"

    assert solve_f(3, 3, "aaa") == "aaa"
    assert solve_f(5, 3, "aaaaa") == "aaa"
    assert solve_f(5, 3, "abcde") == "abc"
    assert solve_f(5, 3, "edcba") == "cba"

    assert solve_f(7, 3, "abcdabc") == "aab"


def test_rmq_build():
    assert RMQ([3]).data[:1] == [3]
    assert RMQ([3, 1]).data[:3] == [1, 3, 1]
    assert RMQ([3, 1, 2]).data[:6] == [1, 1, 2, 3, 1, 2]
    assert RMQ([1, 3, 1, 2]).data[:7] == [1, 1, 1, 1, 3, 1, 2]
    assert RMQ([1, 3, 1, 2, 3], inf=100).data[:12] == [1, 1, 3, 1, 1, 3, 100, 1, 3, 1, 2, 3]


def test_rmq_query():
    rmq = RMQ([1, 3, 1, 0, 3], inf=100)
    assert rmq.query(q_left=0, q_right=5) == 0
    assert rmq.query(q_left=0, q_right=3) == 1
    assert rmq.query(q_left=4, q_right=5) == 3
    assert rmq.query(q_left=5, q_right=5) == 100
