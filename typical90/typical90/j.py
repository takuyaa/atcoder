from typing import List, Tuple


def main():
    N = int(input())

    C = [0] * N
    P = [0] * N
    for i in range(N):
        C[i], P[i] = [int(s) for s in input().split()]

    Q = int(input())

    L = [0] * Q
    R = [0] * Q
    for i in range(Q):
        L[i], R[i] = [int(s) for s in input().split()]

    ans = solve_j(C, P, L, R)
    for t in ans:
        print(f"{t[0]} {t[1]}")


def solve_j(C: List[int], P: List[int], L: List[int], R: List[int]) -> List[Tuple[int, int]]:
    assert len(C) == len(P)
    assert len(L) == len(R)

    cum_sum_1: List[int] = [0] * (len(P) + 1)
    cum_sum_2: List[int] = [0] * (len(P) + 1)

    for i in range(len(P)):
        if C[i] == 1:
            cum_sum_1[i + 1] = cum_sum_1[i] + P[i]
            cum_sum_2[i + 1] = cum_sum_2[i]
        else:
            cum_sum_1[i + 1] = cum_sum_1[i]
            cum_sum_2[i + 1] = cum_sum_2[i] + P[i]

    ans = [] * len(L)
    for j in range(len(L)):
        sum_1 = cum_sum_1[R[j]] - cum_sum_1[L[j] - 1]
        sum_2 = cum_sum_2[R[j]] - cum_sum_2[L[j] - 1]
        ans.append((sum_1, sum_2))

    return ans


if __name__ == "__main__":
    main()
