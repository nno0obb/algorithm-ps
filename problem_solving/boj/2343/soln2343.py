"""
# 백준
# No. 2343
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    # Logic
    l = max(sum(A) // M, *A)
    r = sum(A)
    ans = float("inf")
    while l <= r:
        m = (l + r) // 2

        cnt, vol = 1, 0
        for a in A:
            if vol + a > m:
                cnt += 1
                vol = a
            else:
                vol += a

        if cnt <= M:
            ans = min(ans, m)
            r = m - 1
        else:
            l = m + 1

    # Output
    print(ans)


if __name__ == "__main__":
    main()
