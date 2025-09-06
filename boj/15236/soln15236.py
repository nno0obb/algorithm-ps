"""
# 백준
# No. 15236
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())

    # Logic
    ans = 0
    for i in range(1, N + 1):
        ans += i * (i + 1)
        ans += i * (i + 1) // 2

    # Output
    print(ans)


if __name__ == "__main__":
    main()
