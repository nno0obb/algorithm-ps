"""
# 백준
# No. 16112
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # Logic
    A.sort()
    ans = 0
    for i, a in enumerate(A):
        ans += a * min(i, K)

    # Output
    print(ans)


if __name__ == "__main__":
    main()
