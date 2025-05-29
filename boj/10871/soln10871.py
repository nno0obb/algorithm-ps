"""
# 백준
# No. 10871 
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N, X = map(int, input().split())
    A = list(map(int, input().split()))

    # Logic
    ans = filter(lambda a: a < X, A)

    # Output
    print(*ans)


if __name__ == "__main__":
    main()
