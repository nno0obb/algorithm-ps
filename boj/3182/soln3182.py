"""
# 백준
# No. 3182 
# Python 3.11.9
# by "nno0obb"
"""

# Global Variables
max_N = 1000
is_visited = [None] + [False] * max_N
is_cycle = [None] + [False] * max_N
C = [-1] + [0] * max_N
D = [-1] + [0] * max_N


def dfs(x, p):
    if is_visited[x]:
        if p.index(x) != len(p) - 1:  # Cycle
            s = p.index(x)
            e = len(p) - 1
            len_cycle = e - s
            for i in p[s:e]:
                is_cycle[i] = True
                D[i] = len_cycle
            return len_cycle
        else:
            return D[x]
    is_visited[x] = True
    D[x] = dfs(C[x], p + [C[x]]) + 1
    if is_cycle[x]:
        D[x] = D[C[x]]
    return D[x]


def main():
    # Input
    N = int(input())
    for i in range(1, N + 1):
        C[i] = int(input())

    # Logic
    for i in range(1, N + 1):
        D[i] = dfs(i, [i])

    max_D = max(D)
    ans = D.index(max_D)

    # Output
    print(ans)


if __name__ == "__main__":
    main()
