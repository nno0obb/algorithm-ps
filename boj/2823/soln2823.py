"""
# 백준
# No. 2823
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    R, C = map(int, input().split())
    M = [input() for _ in range(R)]

    # Logic
    dead_end_count = 0
    for cy in range(R):
        for cx in range(C):
            if M[cy][cx] == ".":
                open_dir_count = 0
                for dy, dx in [(+1, 0), (0, +1), (-1, 0), (0, -1)]:
                    ay, ax = cy + dy, cx + dx
                    if 0 <= ay < R and 0 <= ax < C:
                        if M[ay][ax] == ".":
                            open_dir_count += 1
                if open_dir_count <= 1:
                    dead_end_count += 1

    ans = 0 if dead_end_count == 0 else 1

    # Output
    print(ans)


if __name__ == "__main__":
    main()
