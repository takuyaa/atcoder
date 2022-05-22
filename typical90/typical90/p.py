def main():
    N = int(input())
    A, B, C = [int(s) for s in input().split()]
    ans = solve_p(N, A, B, C)
    print(f"{ans}")


def solve_p(N: int, A: int, B: int, C: int) -> int:
    for k in range(3, 10000):
        for a in range(1, k):
            for b in range(1, (k - a)):
                c = k - a - b
                if A * a + B * b + C * c == N:
                    return k

    return -1


if __name__ == "__main__":
    main()
