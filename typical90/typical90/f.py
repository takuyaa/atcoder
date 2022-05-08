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

    min_str = ""
    head_pos = 0
    for k in range(K, 0, -1):
        (_, min_idx) = rmq.query(q_left=head_pos, q_right=(N - k + 1))
        assert len(min_idx) > 0

        min_pos = min_idx[0]
        min_str += S[min_pos]
        head_pos = min_pos + 1

    return min_str


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


if __name__ == "__main__":
    main()
