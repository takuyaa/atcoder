def main():
    s = input()

    while len(s) != 0:
        if s.endswith("dream") or s.endswith("erase"):
            s = s[0:len(s)-5]
            continue
        elif s.endswith("eraser"):
            s = s[0:len(s)-6]
            continue
        elif s.endswith("dreamer"):
            s = s[0:len(s)-7]
            continue
        else:
            print("NO")
            return
    print("YES")

if __name__ == "__main__":
    main()
