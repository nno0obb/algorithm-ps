"""
# 백준
# No. 1032 
# Python 3.11.11
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())
    filenames = [input() for _ in range(N)]

    # Logic
    pattern = filenames[0]
    for i in range(1, N):
        pattern = "".join(list(map(lambda x, y: x if x == y else "?", pattern, filenames[i])))

    # Output
    print(pattern)


if __name__ == "__main__":
    main()
