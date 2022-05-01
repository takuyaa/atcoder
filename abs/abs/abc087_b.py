def main():
    a, b, c, x = [int(input()) for _ in range(4)]
    ret = 0
    for a_i in range(a + 1):
        for b_i in range(b + 1):
            for c_i in range(c + 1):
                if a_i * 500 + b_i * 100 + c_i * 50 == x:
                    ret = ret + 1
    print(ret)

if __name__ == "__main__":
    main()
