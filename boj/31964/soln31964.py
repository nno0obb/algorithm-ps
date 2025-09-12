"""
# 백준
# No. 31964
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())
    X = list(map(int, input().split()))
    T = list(map(int, input().split()))

    # Logic
    ans = max(X[-1], T[-1])
    for i in range(N - 2, -1, -1):
        ans = max(ans + X[i + 1] - X[i], T[i])
    ans += X[0]

    # Output
    print(ans)


if __name__ == "__main__":
    main()
