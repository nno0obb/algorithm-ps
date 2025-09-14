"""
# 백준
# No. 4589
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N, ans = int(input()), []
    for _ in range(N):
        A, B, C = map(int, input().split())

        # Logic
        if A < B < C or C < B < A:
            ans.append("Ordered")
        else:
            ans.append("Unordered")

    # Output
    print("Gnomes:")
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
