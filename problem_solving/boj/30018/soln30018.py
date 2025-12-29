"""
# 백준
# No. 30018
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # Logic
    ans = sum(abs(a - b) for a, b in zip(A, B)) // 2

    # Output
    print(ans)


if __name__ == "__main__":
    main()
