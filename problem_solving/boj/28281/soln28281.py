"""
# 백준
# No. 28281
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N, X = map(int, input().split())
    As = list(map(int, input().split()))

    # Logic
    cands = [sum(As[i : i + 2]) * X for i in range(N - 1)]
    ans = min(cands)

    # Output
    print(ans)


if __name__ == "__main__":
    main()
