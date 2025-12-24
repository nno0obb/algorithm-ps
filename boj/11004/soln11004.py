"""
# 백준
# No. 11004
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # Logic
    A.sort()

    # Output
    print(A[K - 1])


if __name__ == "__main__":
    main()
