"""
# 백준
# No. 27496
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N, L = map(int, input().split())
    A = list(map(int, input().split()))

    # Logic
    cnt, bac = 0, 0
    for i in range(N):
        bac += A[i]
        if i >= L:
            bac -= A[i - L]
        if 129 <= bac <= 138:
            cnt += 1

    # Output
    print(cnt)


if __name__ == "__main__":
    main()
