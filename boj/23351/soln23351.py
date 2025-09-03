"""
# 백준
# No. 23351
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N, K, A, B = map(int, input().split())

    # Logic
    C = N // A

    ans = 0
    while K:
        if K <= (C - 1):
            ans += K
            break
        K -= C - 1
        ans += C - 1

        K += B - 1
        ans += 1

    # Output
    print(ans)


if __name__ == "__main__":
    main()
