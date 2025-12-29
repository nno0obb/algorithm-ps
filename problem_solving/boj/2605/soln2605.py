"""
# 백준
# No. 2605
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())
    A = list(map(int, input().split()))

    # Logic
    B = []
    for i, a in enumerate(A, start=1):
        B.insert(a, i)
    B.reverse()

    # Output
    print(*B)


if __name__ == "__main__":
    main()
