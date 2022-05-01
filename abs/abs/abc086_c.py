def main():
    n = int(input())

    (ti, xi, yi) = (0, 0, 0)
    for _ in range(n):
        t, x, y = [int(s) for s in input().split()]
        if not can_travel(t - ti, abs(x - xi), abs(y - yi)):
            print("No")
            return
        else:
            (ti, xi, yi) = (t, x, y)

    print("Yes")

# 0 <= t, x, y
def can_travel(t, x, y: int) -> bool:
    if x + y > t:
        return False
    play_time = x + y - t
    return play_time % 2 == 0

if __name__ == "__main__":
    main()
