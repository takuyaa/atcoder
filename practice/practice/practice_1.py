def main():
    a = int(input())
    b, c = [int(s) for s in input().split()]
    s = input()
    print(f"{a+b+c} {s}")

if __name__ == "__main__":
    main()
