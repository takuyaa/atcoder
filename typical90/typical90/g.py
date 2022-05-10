import sys
from typing import Generator, List


def main():
    _ = int(input())
    A = [int(s) for s in input().split()]
    Q = int(input())
    B = [int(input()) for _ in range(Q)]

    [print(f"{score}") for score in solve_g(A, B)]


def solve_g(A: List[int], B: List[int]) -> Generator[int, None, None]:
    A.sort()
    for b in B:
        score = min_score(A, b)
        yield score


def min_score(A: List[int], b: int) -> int:
    l = 0
    r = len(A)
    m = 0

    while l < r:
        m = (l + r) // 2
        if b < A[m]:
            r = m
        elif b > A[m]:
            l = m + 1
        else:
            return 0

    ls = abs(A[m - 1] - b) if 0 < m else sys.maxsize
    ms = abs(A[m] - b)
    rs = abs(A[m + 1] - b) if m < len(A) - 2 else sys.maxsize
    return min(ls, ms, rs)


if __name__ == "__main__":
    main()
