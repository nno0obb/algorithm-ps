"""
# 백준
# No. 30802
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())
    S, M, L, XL, XXL, XXXL = map(int, input().split())
    T, P = map(int, input().split())

    # Logic
    ans_1, ans_2 = 0, (0, 0)
    for s in [S, M, L, XL, XXL, XXXL]:
        ans_1 += (s + T - 1) // T
    ans_2 = divmod(N, P)

    # Output
    print(ans_1)
    print(*ans_2)


if __name__ == "__main__":
    main()
