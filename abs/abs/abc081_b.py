def main():
    _ = int(input())
    a = [int(s) for s in input().split()]
    
    count = 0
    while all([a_i % 2 == 0 for a_i in a]):
        a = [a_i // 2 for a_i in a]
        count = count + 1

    print(count)

if __name__ == "__main__":
    main()
