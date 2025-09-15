"""
# 백준
# No. 6186
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    R, C = map(int, input().split())
    P = [input() for _ in range(R)]

    # Logic
    ans = 0
    is_visited = set()
    for i in range(R):
        for j in range(C):
            if P[i][j] == "#" and (i, j) not in is_visited:
                ans += 1
                for dy, dx in [(+1, 0), (0, +1)]:
                    ay, ax = i + dy, j + dx
                    if 0 <= ay < R and 0 <= ax < C:
                        if P[ay][ax] == "#" and (ay, ax) not in is_visited:
                            is_visited.add((ay, ax))
                            break

    # Output
    print(ans)


if __name__ == "__main__":
    main()
