"""
# 백준
# No. 14732
# Python 3.11.9
# by "nno0obb"
"""

# Gloval Variables
MAX_X = 500
MAX_Y = 500
B = [[False] * MAX_Y for _ in range(MAX_X)]


def main():
    # Input
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    # Logic
    for x1, y1, x2, y2 in A:
        for y in range(y1, y2):
            for x in range(x1, x2):
                B[y][x] = True

    ans = 0
    for row in B:
        ans += row.count(True)

    # Output
    print(ans)


if __name__ == "__main__":
    main()
