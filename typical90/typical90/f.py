import math
import sys
from typing import List, Tuple

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

    rmq = RMQ(array=[ord(c) for c in S])

    return sub(N, S, rmq, left=0, k=K)


class RMQ:
    def __init__(self, array: List[int], inf: int = sys.maxsize) -> None:
        self.inf: int = inf
        self.height: int = 0
        self.n_leaves: int = 0
        self.data: List[int]
        self.indices: List[List[int]]

        if len(array) == 0:
            self.data = []
            return

        # hight of segment tree excluding leaves
        self.height = math.ceil(math.log2(len(array)))

        # number of leaf nodes of segment tree
        self.n_leaves = 2**self.height

        # internal data representation for segment tree
        # number of all elements of the segment tree is `2 * N - 1`
        self.data = [inf] * (2 * self.n_leaves - 1)
        self.indices = [[] for _ in range(2 * self.n_leaves - 1)]

        # init leaves
        for i in range(len(array)):
            self.data[(2**self.height - 1) + i] = array[i]
            self.indices[(2**self.height - 1) + i] = [i]

        for i in range(self.n_leaves - 2, -1, -1):
            if self.data[2 * i + 1] < self.data[2 * i + 2]:
                self.data[i] = self.data[2 * i + 1]
                self.indices[i].extend(self.indices[2 * i + 1])
            elif self.data[2 * i + 1] > self.data[2 * i + 2]:
                self.data[i] = self.data[2 * i + 2]
                self.indices[i].extend(self.indices[2 * i + 2])
            else:
                self.data[i] = self.data[2 * i + 1]
                self.indices[i].extend(self.indices[2 * i + 1])
                self.indices[i].extend(self.indices[2 * i + 2])

    def query(self, q_left: int, q_right: int) -> Tuple[int, List[int]]:
        return self._query(q_left, q_right, node=0, left=0, right=self.n_leaves)

    def _query(self, q_left: int, q_right: int, node: int, left: int, right: int) -> Tuple[int, List[int]]:
        if q_left >= right or q_right <= left:
            return (self.inf, [])
        elif q_left <= left and q_right >= right:
            return (self.data[node], self.indices[node])

        (l_min, l_indices) = self._query(q_left, q_right, node=(node * 2 + 1), left=left, right=((left + right) // 2))
        (r_min, r_indices) = self._query(q_left, q_right, node=(node * 2 + 2), left=((left + right) // 2), right=right)

        if l_min < r_min:
            return (l_min, l_indices)
        elif l_min > r_min:
            return (r_min, r_indices)
        else:
            return (l_min, l_indices + r_indices)


def sub(N: int, S: str, rmq: RMQ, left: int, k: int) -> str:
    if k == 0:
        return ""
    elif k == (N - left):
        return S[left:N]

    (min_ch, min_idx) = rmq.query(q_left=left, q_right=(N - k + 1))

    str_min = "{"  # "{" is bigger than "zzz..."
    for i in min_idx:
        sub_ans = chr(min_ch) + sub(N=N, S=S, rmq=rmq, left=(i + 1), k=(k - 1))
        assert len(sub_ans) == k

        if sub_ans < str_min:
            str_min = sub_ans

    return str_min


if __name__ == "__main__":
    main()
