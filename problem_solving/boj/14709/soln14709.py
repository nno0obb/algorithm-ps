"""
# 백준
# No. 14709
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())
    S = [tuple(map(int, sorted(input().split()))) for _ in range(N)]

    # Logic
    ans = "Woof-meow-tweet-squeek"
    if (1, 3) in S and (1, 4) in S and (3, 4) in S:
        if len(S) == 3:
            ans = "Wa-pa-pa-pa-pa-pa-pow!"

    # Output
    print(ans)


if __name__ == "__main__":
    main()
