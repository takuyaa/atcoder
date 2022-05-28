def main():
    S = input()
    ans = solve_a(S)
    print(f"{ans}")


def solve_a(S: str) -> str:
    assert 1 <= len(S) and len(S) <= 3
    return "".join([S for _ in range(6 // len(S))])


if __name__ == "__main__":
    main()
