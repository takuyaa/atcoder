import math
import sys
from typing import List

sys.setrecursionlimit(1 << 24)


def main():
    N, K = [int(s) for s in input().split()]
    S = input()

    ans = solve_f(N, K, S)
    print(f"{ans}")


def solve_f(N: int, K: int, S: str) -> str:
    if K == 0:
        return ""
    elif K == N:
        return S

    s_ch = min(S[: N - K + 1])

    str_min = "{"  # "{" is bigger than "z"
    for i in range(N - K, -1, -1):
        if S[i] != s_ch:
            continue

        sub_ans = s_ch + solve_f(N - i - 1, K - 1, S[i + 1 :])
        assert len(sub_ans) == K

        if sub_ans < str_min:
            str_min = sub_ans

    return str_min


class RMQ:
    def __init__(self, array: List[int], inf: int = sys.maxsize) -> None:
        self.inf: int = inf
        self.height: int = 0
        self.n_leaves: int = 0
        self.data: List[int]

        if len(array) == 0:
            self.data = []
            return

        # hight of segment tree excluding leaves
        self.height = math.ceil(math.log2(len(array)))

        # number of leaf nodes of segment tree
        self.n_leaves = 2**self.height

        # internal data representation for segment tree
        # number of all elements of the segment tree is `2 * N - 1`
        self.data = [inf] * (2**self.n_leaves - 1)

        # init leaves
        for i in range(len(array)):
            self.data[(2**self.height - 1) + i] = array[i]

        for i in range(self.n_leaves - 2, -1, -1):
            self.data[i] = min(self.data[2 * i + 1], self.data[2 * i + 2])

    def query(self, q_left: int, q_right: int) -> int:
        return self._query(q_left, q_right, node=0, left=0, right=self.n_leaves)

    def _query(self, q_left: int, q_right: int, node: int, left: int, right: int) -> int:
        if q_left >= right or q_right <= left:
            return self.inf
        elif q_left <= left and q_right >= right:
            return self.data[node]

        min_l = self._query(q_left, q_right, node=(node * 2 + 1), left=left, right=((left + right) // 2))
        min_r = self._query(q_left, q_right, node=(node * 2 + 2), left=((left + right) // 2), right=right)

        return min(min_l, min_r)


if __name__ == "__main__":
    main()
