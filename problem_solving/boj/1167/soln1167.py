"""
# 백준
# No. 1167
# Python 3.11.9
# by "nno0obb"
"""

import sys
from collections import defaultdict, deque


def main():
    # Input
    V = int(input())
    G = defaultdict(list)
    for _ in range(V):
        L = list(map(int, sys.stdin.readline().strip().split()))
        v1 = L[0]
        for v2, dist in zip(L[1::2], L[2::2]):
            G[v1].append((v2, dist))

    # Logic
    def bfs(v: int) -> (int, int):
        nonlocal G

        is_visited = [False] * (V + 1)
        D = [-1] * (V + 1)

        que = deque()

        que.append((v, 0))
        is_visited[v] = True
        D[v] = 0

        while que:
            cv, cd = que.popleft()

            for nv, nd in G[cv]:
                if not is_visited[nv]:
                    que.append((nv, cd + nd))
                    is_visited[nv] = True
                    D[nv] = cd + nd

        max_dist = max(D)
        max_idx = D.index(max_dist)
        return max_idx, max_dist

    max_idx, _ = bfs(1)
    _, ans = bfs(max_idx)

    # Output
    print(ans)


if __name__ == "__main__":
    main()
