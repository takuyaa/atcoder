from typing import List


def main():
    H, W = [int(s) for s in input().split()]

    A = [] * H
    for _ in range(H):
        A.append([int(s) for s in input().split()])

    B = solve_d(A, H, W)
    for i in range(H):
        print(" ".join([str(e) for e in B[i]]))


def solve_d(A: List[List[int]], H: int, W: int) -> List[List[int]]:
    sum_row: List[int] = [sum(row) for row in A]

    sum_col: List[int] = []
    for j in range(W):
        sum_j = 0
        for i in range(H):
            sum_j += A[i][j]
        sum_col.append(sum_j)

    B: List[List[int]] = [] * H
    for i in range(H):
        B.append([sum_row[i] + sum_col[j] - A[i][j] for j in range(W)])

    return B


if __name__ == "__main__":
    main()
