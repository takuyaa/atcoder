def main():
    N = int(input())
    A, B, C = [int(s) for s in input().split()]
    ans = solve_p(N, A, B, C)
    print(f"{ans}")


def solve_p(N: int, A: int, B: int, C: int) -> int:
    min_coins = 10000

    max_a = min(N // A, 9999)
    for a in range(0, max_a + 1):
        rest_bc = N - A * a
        if rest_bc < 0:
            continue

        max_b = min(rest_bc // B, 9999 - a)
        for b in range(0, max_b + 1):
            rest_c = rest_bc - B * b
            if rest_c < 0 or rest_c % C != 0:
                continue

            c = rest_c // C
            coins = a + b + c
            if coins < min_coins:
                min_coins = coins

    return min_coins


if __name__ == "__main__":
    main()
