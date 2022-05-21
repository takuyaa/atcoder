from typing import List


def main():
    _ = int(input())
    A = [int(s) for s in input().split()]
    B = [int(s) for s in input().split()]

    ans = solve_n(A, B)
    print(f"{ans}")


def solve_n(A: List[int], B: List[int]) -> int:
    assert len(A) == len(B)

    A.sort()
    B.sort()

    return sum((abs(A[i] - B[i]) for i in range(len(A))))


if __name__ == "__main__":
    main()
