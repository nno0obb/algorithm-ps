"""
# 백준
# No. 11724
# Python 3.11.9
# by "nno0obb"
"""

import sys
from collections import defaultdict


def main():
    # Input
    N, M = map(int, input().split())
    G = defaultdict(list)
    for _ in range(M):
        u, v = map(int, sys.stdin.readline().strip().split())
        G[u].append(v)
        G[v].append(u)

    # Logic
    is_visited = [False] * (N + 1)
    ans = 0
    for i in range(1, N + 1):
        if not is_visited[i]:
            ans += 1

            stack = [i]
            is_visited[i] = True
            while stack:
                curr = stack.pop()
                for _next in G[curr]:
                    if not is_visited[_next]:
                        stack.append(_next)
                        is_visited[_next] = True

    # Output
    print(ans)


if __name__ == "__main__":
    main()
