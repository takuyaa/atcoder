def main():
    n = int(input())
    d = [int(input()) for _ in range(n)]

    print(len(set(d)))

if __name__ == "__main__":
    main()
