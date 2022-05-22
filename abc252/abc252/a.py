def main():
    N = int(input())
    ans = solve_a(N)
    print(f"{ans}")


def solve_a(N: int) -> str:
    return chr(N)


if __name__ == "__main__":
    main()
