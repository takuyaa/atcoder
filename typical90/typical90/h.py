from typing import List


def main():
    _ = int(input())
    S = input()
    ans = solve_h(S)
    print(f"{ans}")


def solve_h(S: str) -> int:
    T = "atcoder"

    counts: List[List[int]] = [[0] * (len(T) + 1) for _ in range(len(S) + 1)]

    # initialize the first state for each position
    for state in counts:
        state[0] = 1  # of initial state (j == 0)

    # DP for each position
    for i in range(1, len(S) + 1):
        ch = S[i - 1]
        for j in range(1, len(T) + 1):
            if T[j - 1] == ch:
                counts[i][j] += counts[i - 1][j] + counts[i - 1][j - 1]
            else:
                counts[i][j] += counts[i - 1][j]

    return counts[-1][-1] % (10**9 + 7)


if __name__ == "__main__":
    main()
