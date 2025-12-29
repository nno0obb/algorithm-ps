"""
# 백준
# No. 1260
# Python 3.11.9
# by "nno0obb"
"""

import sys
from collections import deque

sys.setrecursionlimit(1_000_000)


# Global Variables
max_N = 1000
E = [[] for _ in range(max_N + 1)]
is_visited = [False] * (max_N + 1)
L_dfs, L_bfs = [], []


def dfs(c):
    is_visited[c] = True
    L_dfs.append(c)
    for n in E[c]:
        if not is_visited[n]:
            dfs(n)


def bfs(s):
    que = deque([s])
    is_visited[s] = True
    L_bfs.append(s)
    while que:
        c = que.popleft()
        for n in E[c]:
            if not is_visited[n]:
                que.append(n)
                is_visited[n] = True
                L_bfs.append(n)


def main():
    global is_visited

    # Input
    N, M, V = map(int, input().split())
    for _ in range(M):
        n, m = map(int, input().split())
        E[n].append(m)
        E[m].append(n)

    # Logic
    for i in range(1, N + 1):
        E[i].sort()

    dfs(V)
    is_visited = [False] * (N + 1)
    bfs(V)

    # Output
    print(*L_dfs)
    print(*L_bfs)


if __name__ == "__main__":
    main()
