"""
# 백준
# No. 1018
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N, M = map(int, input().split())
    board = [input() for _ in range(N)]

    # Logic
    ans = 64
    for i in range(N - 7):
        for j in range(M - 7):
            chessboard = [row[j : j + 8] for row in board[i : i + 8]]
            count = 0
            for y in range(8):
                for x in range(8):
                    if (y + x) % 2:  # 홀수칸, W
                        if chessboard[y][x] != "W":
                            count += 1
                    else:  # 짝수칸, B
                        if chessboard[y][x] != "B":
                            count += 1
            ans = min(ans, count, 64 - count)

    # Output
    print(ans)


if __name__ == "__main__":
    main()
