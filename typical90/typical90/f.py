import sys

sys.setrecursionlimit(1 << 24)


def main():
    N, K = [int(s) for s in input().split()]
    S = input()

    ans = solve_f(N, K, S)
    print(f"{ans}")


def solve_f(N: int, K: int, S: str) -> str:
    if K == 0:
        return ""
    elif K == N:
        return S

    s_ch = min(S[: N - K + 1])

    str_min = "{"  # "{" is bigger than "z"
    for i in range(N - K, -1, -1):
        if S[i] != s_ch:
            continue

        sub_ans = s_ch + solve_f(N - i - 1, K - 1, S[i + 1 :])
        assert len(sub_ans) == K

        if sub_ans < str_min:
            str_min = sub_ans

    return str_min


if __name__ == "__main__":
    main()
