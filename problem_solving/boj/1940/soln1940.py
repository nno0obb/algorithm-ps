"""
# 백준
# No. 1940
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())
    M = int(input())
    A = list(map(int, input().split()))

    # Logic
    A.sort()
    ans, sdx, edx = 0, 0, N - 1
    while sdx < edx:
        if A[sdx] + A[edx] < M:
            sdx += 1
        elif A[sdx] + A[edx] > M:
            edx -= 1
        else:
            ans += 1
            sdx += 1
            edx -= 1

    # Output
    print(ans)


if __name__ == "__main__":
    main()
