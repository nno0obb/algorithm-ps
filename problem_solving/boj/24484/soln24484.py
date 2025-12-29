"""
# 백준
# No. 24484 
# Python 3.11.9
# by "nno0obb"
"""

import sys

sys.setrecursionlimit(1_000_000)


# Global Variables
max_N = 100_000 + 1
visited = [False] * max_N
T = [0] * max_N
D = [-1] * max_N
cnt = 1


def dfs(V, E, R, depth):
    global visited, T, D, cnt
    visited[R] = True
    T[R] = cnt
    D[R] = depth
    cnt += 1
    for x in sorted(E[R], reverse=True):
        if not visited[x]:
            dfs(V, E, x, depth + 1)


def main():
    # Input
    N, M, R = map(int, input().split())
    E = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v = map(int, sys.stdin.readline().split())
        E[u].append(v)
        E[v].append(u)

    # Logic
    dfs(N, E, R, depth=0)
    ans = 0
    for i in range(1, N + 1):
        ans += D[i] * T[i]

    # Output
    print(ans)


if __name__ == "__main__":
    main()
