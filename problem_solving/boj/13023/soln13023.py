"""
# 백준
# No. 13023
# Python 3.11.9
# by "nno0obb"
"""

import sys
from collections import defaultdict

sys.setrecursionlimit(1_000_000)


def main():
    # Input
    N, M = map(int, input().split())
    AB = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]

    # Logic
    G = defaultdict(list)
    for a, b in AB:
        G[a].append(b)
        G[b].append(a)
    is_visited = [False] * N
    ans = 0

    def dfs(curr, curr_depth):
        nonlocal ans, is_visited

        if curr_depth == 4:
            ans = 1
            return

        for _next in G[curr]:
            if not is_visited[_next]:
                is_visited[_next] = True
                dfs(_next, curr_depth + 1)
                is_visited[_next] = False

    for i in range(N):
        is_visited[i] = True
        dfs(i, 0)
        is_visited[i] = False

        if ans == 1:  # 📌
            break

    # Output
    print(ans)


if __name__ == "__main__":
    main()
