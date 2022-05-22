from typing import List


def main():
    N, K = [int(s) for s in input().split()]
    A = [int(s) for s in input().split()]
    B = [int(s) for s in input().split()]
    assert len(A) == N
    assert len(B) == K

    ans = solve_b(A, B)
    if ans:
        print("Yes")
    else:
        print("No")


def solve_b(A: List[int], B: List[int]) -> bool:
    max_A = max(A)
    set_B = set(B)

    for i, a in enumerate(A):
        if a == max_A and (i + 1) in set_B:
            return True

    return False


if __name__ == "__main__":
    main()
