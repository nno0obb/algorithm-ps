"""
# 백준
# No. 2875
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N, M, K = map(int, input().split())

    # Logic
    ans = min(N // 2, M)
    K -= (N - ans * 2) + (M - ans)
    if K > 0:
        ans -= (K + 2) // 3

    # Output
    print(ans)


if __name__ == "__main__":
    main()
