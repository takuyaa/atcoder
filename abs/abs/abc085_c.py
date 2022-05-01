def main():
    N, Y = [int(s) for s in input().split()]

    for x in range(N + 1):
        for y in range(N - x + 1):
            z = N - x - y
            if x * 10000 + y * 5000 + z * 1000 == Y:
                print(f"{x} {y} {z}")
                return
    
    print("-1 -1 -1")

if __name__ == "__main__":
    main()
