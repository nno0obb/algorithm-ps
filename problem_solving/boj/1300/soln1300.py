"""
# 백준
# No. 1300
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())
    K = int(input())

    # Logic
    ldx, rdx = 1, K
    ans = -1
    while ldx <= rdx:
        mdx = (ldx + rdx) // 2

        cnt = 0
        for i in range(1, N + 1):
            cnt += min(mdx // i, N)

        if cnt < K:
            ldx = mdx + 1
        else:
            rdx = mdx - 1
            ans = mdx

    # Output
    print(ans)

    # Hint
    # 1 <= B[k] <= K


if __name__ == "__main__":
    main()
