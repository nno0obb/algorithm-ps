"""
# 백준
# No. 20186
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # Logic
    A.sort()
    ans = sum(A[-K:]) - ((K - 1) * K // 2)

    # Output
    print(ans)


if __name__ == "__main__":
    main()
