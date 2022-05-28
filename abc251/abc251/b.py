import itertools
from typing import List, Set


def main():
    N, W = [int(s) for s in input().split()]
    A = [int(s) for s in input().split()]
    assert len(A) == N

    ans = solve_b(A, W)
    print(f"{ans}")


def solve_b(A: List[int], W: int) -> int:
    ans: Set[int] = set()

    for a in A:
        if a <= W:
            ans.add(a)

    if len(A) < 2:
        return len(ans)

    for i, j in itertools.combinations(range(len(A)), 2):
        s = A[i] + A[j]
        if s <= W:
            ans.add(s)

    if len(A) < 3:
        return len(ans)

    for i, j, k in itertools.combinations(range(len(A)), 3):
        s = A[i] + A[j] + A[k]
        if s <= W:
            ans.add(s)

    return len(ans)


if __name__ == "__main__":
    main()
