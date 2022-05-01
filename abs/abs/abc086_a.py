def main():
    a, b = [int(s) for s in input().split()]

    if (a * b) % 2 == 0:
        print("Even")
    else:
        print("Odd")

if __name__ == "__main__":
    main()
