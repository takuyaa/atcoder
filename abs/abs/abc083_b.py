def main():
    n, a, b = [int(s) for s in input().split()]

    sum = 0
    for i in range(1, n + 1):
        q = i
        r_sum = 0
        while q != 0:
            r_sum += q % 10
            q = q // 10
        if a <= r_sum and r_sum <= b:
            sum += i
    print(sum)

if __name__ == "__main__":
    main()
