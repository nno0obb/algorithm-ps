"""
# 백준
# No. 2667
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())
    M = [list(map(int, list(input()))) for _ in range(N)]

    # Logic
    blocks, is_visited = [], set()
    for i in range(N):
        for j in range(N):
            if M[i][j] == 1 and (i, j) not in is_visited:
                que, cnt = [(i, j)], 0
                is_visited.add((i, j))
                while que:
                    cy, cx = que.pop()
                    cnt += 1
                    for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                        ny, nx = cy + dy, cx + dx
                        if 0 <= ny < N and 0 <= nx < N:
                            if M[ny][nx] == 1 and (ny, nx) not in is_visited:
                                que.append((ny, nx))
                                is_visited.add((ny, nx))
                blocks.append(cnt)

    # Output
    print(len(blocks))
    print(*sorted(blocks), sep="\n")


if __name__ == "__main__":
    main()
