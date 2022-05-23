from typing import List


def main():
    N = int(input())
    S = [input() for _ in range(N)]
    ans = solve_c(S)
    print(f"{ans}")


def solve_c(S: List[str]) -> int:
    times = [0] * 10
    for i in range(0, 10):
        indices: List[int] = [s.find(str(i)) for s in S]
        indices.sort()
        assert len(S) == len(indices)

        pos = indices.pop(0)
        times[i] += pos

        while 0 < len(indices):
            nearest_dist = 11
            nearest_pos = -1
            for j in indices:
                if pos < j and j - pos < nearest_dist:
                    nearest_pos = j
                    nearest_dist = j - pos
                elif j < pos and 10 - (pos - j) < nearest_dist:
                    nearest_pos = j
                    nearest_dist = 10 - (pos - j)
                elif j == pos and 10 < nearest_dist:
                    nearest_pos = j
                    nearest_dist = 10
            assert nearest_dist < 11
            assert 0 <= nearest_pos

            pos = nearest_pos
            times[i] += nearest_dist
            indices.remove(nearest_pos)

    return min(times)


if __name__ == "__main__":
    main()
