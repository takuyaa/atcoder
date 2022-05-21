from typing import Generator, List


def main():
    H, W = [int(s) for s in input().split()]
    Q = int(input())

    queries: List[str] = [input() for _ in range(Q)]

    [print(s) for s in solve_l(H, W, queries)]


def solve_l(H: int, W: int, queries: List[str]) -> Generator[str, None, None]:
    p = Painting(H, W)

    for q in queries:
        if q[0] == "1":
            _, r, c = [int(s) for s in q.split()]
            p.paint(i=r, j=c)
        if q[0] == "2":
            _, ra, ca, rb, cb = [int(s) for s in q.split()]
            if p.can_go(ai=ra, aj=ca, bi=rb, bj=cb):
                yield "Yes"
            else:
                yield "No"


# https://github.com/Mitarushi/ACL-Python/blob/master/library/dsu.py
class DSU:
    def __init__(self, n: int) -> None:
        self._n = n
        self.parent_or_size = [-1] * n

    def merge(self, a: int, b: int) -> int:
        assert 0 <= a < self._n
        assert 0 <= b < self._n
        x, y = self.leader(a), self.leader(b)
        if x == y:
            return x
        if -self.parent_or_size[x] < -self.parent_or_size[y]:
            x, y = y, x
        self.parent_or_size[x] += self.parent_or_size[y]
        self.parent_or_size[y] = x
        return x

    def same(self, a: int, b: int) -> bool:
        assert 0 <= a < self._n
        assert 0 <= b < self._n
        return self.leader(a) == self.leader(b)

    def leader(self, a: int) -> int:
        assert 0 <= a < self._n
        stack = []
        while self.parent_or_size[a] >= 0:
            stack.append(a)
            a = self.parent_or_size[a]
        for i in stack:
            self.parent_or_size[i] = a
        return a

    def size(self, a: int) -> int:
        assert 0 <= a < self._n
        return -self.parent_or_size[self.leader(a)]

    def groups(self) -> List[List[int]]:
        leader_buf = [self.leader(i) for i in range(self._n)]
        group_size = [0] * self._n
        for i in leader_buf:
            group_size[i] += 1
        result: List[List[int]] = [[] for _ in range(self._n)]
        for i in range(self._n):
            result[leader_buf[i]].append(i)
        result = [i for i in result if i]
        return result


class Painting:
    H: int
    W: int
    matrix: List[List[bool]]
    dsu: DSU

    def __init__(self, H: int, W: int) -> None:
        self.H = H
        self.W = W

        self.matrix = [[False for _ in range(W + 2)] for _ in range(H + 2)]
        assert len(self.matrix) == H + 2

        self.dsu = DSU((H + 2) * (W + 2))

    def can_go(self, ai: int, aj: int, bi: int, bj: int) -> bool:
        if not self.matrix[ai][aj]:
            return False
        if not self.matrix[bi][bj]:
            return False

        return self.dsu.same(self.dsu_pos(ai, aj), self.dsu_pos(bi, bj))

    def paint(self, i: int, j: int) -> None:
        self.matrix[i][j] = True
        assert 0 < i and i < self.H + 1
        assert 0 < j and j < self.W + 1

        if self.matrix[i - 1][j]:
            self.dsu.merge(self.dsu_pos(i, j), self.dsu_pos(i - 1, j))
        if self.matrix[i + 1][j]:
            self.dsu.merge(self.dsu_pos(i, j), self.dsu_pos(i + 1, j))
        if self.matrix[i][j - 1]:
            self.dsu.merge(self.dsu_pos(i, j), self.dsu_pos(i, j - 1))
        if self.matrix[i][j + 1]:
            self.dsu.merge(self.dsu_pos(i, j), self.dsu_pos(i, j + 1))

    def dsu_pos(self, i: int, j: int) -> int:
        return self.W * i + j


if __name__ == "__main__":
    main()
