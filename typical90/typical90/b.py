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


if __name__ == "__main__":
    main()
