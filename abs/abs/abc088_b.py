def main():
    n = int(input())
    a = [int(s) for s in input().split()]

    a.sort(reverse=True)

    a_score = 0
    b_score = 0
    for i in range(n):
        if i % 2 == 0:
            a_score += a.pop(0)
        else:
            b_score += a.pop(0)

    print(a_score - b_score)

if __name__ == "__main__":
    main()
