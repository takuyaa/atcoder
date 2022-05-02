from typing import List


def main():
    N, L = [int(s) for s in input().split()]
    K = int(input())
    A = [int(s) for s in input().split()]
    assert N == len(A)

    max_score = solve_a(N, L, K, A)

    print(max_score)


def solve_a(N: int, L: int, K: int, A: List[int]) -> int:
    # binary search for score
    left_score = 0
    right_score = L
    while left_score < right_score:
        mid_score: int = ((left_score + right_score) // 2) + 1
        if can_devide(A, K, L, mid_score):
            left_score = mid_score
        else:
            right_score = mid_score - 1
        if left_score == right_score:
            return left_score
    return -1


def can_devide(A: List[int], K: int, L: int, min_length: int) -> bool:
    cuts = 0
    last_cut_pos = 0
    for a in A:
        if cuts >= K:
            break
        if (a - last_cut_pos) >= min_length:
            # cut
            cuts += 1
            last_cut_pos = a

    # last piece
    if L - last_cut_pos < min_length:
        return False

    if cuts >= K:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
