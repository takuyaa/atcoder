import itertools
from typing import Generator, Tuple


def main():
    N = int(input())
    [print(s) for s in solve_b(N=N)]


def solve_b(N: int) -> Generator[str, None, None]:
    if N == 0:
        yield from ()
        return
    for a in itertools.product([1, -1], repeat=N):
        if not is_valid(a):
            continue
        yield "".join(["(" if a_i == 1 else ")" for a_i in a])


def is_valid(a: Tuple[int, ...]) -> bool:
    sum = 0
    for a_i in a:
        sum += a_i
        if sum < 0:
            return False
    return sum == 0


# def solve_b(N: int) -> Generator[str, None, None]:
#     listed: Set[str] = set()
#     for s in gen(N=N, n=N):
#         if s in listed:
#             continue
#         listed.add(s)
#         yield s


# def gen(N: int, n: int) -> Generator[str, None, None]:
#     if n <= 0:
#         yield from ()
#         return
#     elif n % 2 != 0:
#         yield from ()
#         return
#     elif n == 2:
#         yield "()"
#         return

#     # ( S )
#     for s in gen(N, n - 2):
#         yield "(" + s + ")"

#     # S + T
#     for i in range(1, n // 2):
#         s_len = (n // 2) - i
#         t_len = i
#         for s in gen(N, s_len * 2):
#             for t in gen(N, t_len * 2):
#                 yield s + t


if __name__ == "__main__":
    main()
