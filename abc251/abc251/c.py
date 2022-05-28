from typing import List, Set


def main():
    N = int(input())
    S: List[str] = list()
    T: List[int] = list()
    for _ in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))

    ans = solve_c(S, T)
    print(f"{ans}")


def solve_c(S: List[str], T: List[int]) -> int:
    assert len(S) == len(T)

    subs: Set[str] = set()
    highest_score = -1
    highest_index = -1

    for i in range(len(S)):
        if S[i] in subs:
            # not original
            continue
        subs.add(S[i])

        if highest_score < T[i]:
            highest_score = T[i]
            highest_index = i

    return highest_index + 1


if __name__ == "__main__":
    main()
