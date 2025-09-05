"""
# 백준
# No. 16924
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N, M = map(int, input().split())
    B = [list(input()) for _ in range(N)]

    # Logic
    crosses = []
    for i in range(N):
        for j in range(M):
            if B[i][j] == "*":
                s = 1
                while True:
                    if not (i - s >= 0 and i + s < N and j - s >= 0 and j + s < M):
                        break

                    if B[i - s][j] == "*" and B[i + s][j] == "*" and B[i][j - s] == "*" and B[i][j + s] == "*":
                        s += 1
                    else:
                        break
                if s > 1:
                    crosses.append((i, j, s - 1))

    for cross in crosses:
        i, j, s = cross
        B[i][j] = "."
        for d in range(1, s + 1):
            B[i - d][j] = "."
            B[i + d][j] = "."
            B[i][j - d] = "."
            B[i][j + d] = "."

    is_possible = True
    for row in B:
        if "*" in row:
            is_possible = False
            break

    # Output
    if is_possible:
        print(len(crosses))
        for cross in crosses:
            i, j, s = cross
            print(i + 1, j + 1, s)
    else:
        print(-1)


if __name__ == "__main__":
    main()
