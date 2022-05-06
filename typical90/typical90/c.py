import sys
from typing import Dict, List, Set, Tuple


def main():
    N = int(input())

    conn: Dict[int, Set[int]] = dict()
    for _ in range(N - 1):
        a_i, b_i = [int(s) for s in input().split()]

        if a_i not in conn:
            conn[a_i] = set()
        conn[a_i].add(b_i)

        if b_i not in conn:
            conn[b_i] = set()
        conn[b_i].add(a_i)

    max_score = solve_c(conn)
    print(max_score)


def solve_c(conn: Dict[int, Set[int]]) -> int:
    sys.setrecursionlimit(1 << 24)

    if len(conn) == 0:
        return 0

    # DFS is managed by this stack.
    # element: (node_id, parent_node_id, dist_from_start)
    stack: List[Tuple[int, int, int]] = []

    # Calculate farthest node from arbitrary node.
    # Pick the first node as a start node and perform DFS from the node.
    start_node = next(iter(conn.keys()))
    stack.append((start_node, -1, 0))
    farthest_node_from_start, farthest_dist_from_start = find_furthest(
        conn, stack, start_node, farthest_node=start_node, farthest_dist=0
    )

    # Calculate farthest node from the previous node.
    # This is the diameter of this tree.
    stack.append((farthest_node_from_start, -1, 0))
    _, farthest_dist = find_furthest(
        conn, stack, start_node=farthest_dist_from_start, farthest_node=farthest_dist_from_start, farthest_dist=0
    )

    return farthest_dist + 1


def find_furthest(
    conn: Dict[int, Set[int]],
    stack: List[Tuple[int, int, int]],
    start_node: int,
    farthest_node: int,
    farthest_dist: int,
) -> Tuple[int, int]:
    if len(stack) == 0:
        return (farthest_node, farthest_dist)

    # Get target node from stack
    node, parent_node, dist_from_start = stack.pop()

    if node not in conn:
        return (farthest_node, farthest_dist)

    # Push children to stack
    for next_node in conn[node]:
        if next_node == parent_node:
            continue
        stack.append((next_node, node, dist_from_start + 1))

    if dist_from_start > farthest_dist:
        # Recursive call with updating farthest node
        return find_furthest(conn, stack, start_node, farthest_node=node, farthest_dist=dist_from_start)
    else:
        return find_furthest(conn, stack, start_node, farthest_node, farthest_dist)


if __name__ == "__main__":
    main()
