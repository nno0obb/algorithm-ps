"""
# 백준
# No. 11134
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    T = int(input())
    for _ in range(T):
        N, C = map(int, input().split())

        # Logic
        ans = (N + C - 1) // C

        # Output
        print(ans)


if __name__ == "__main__":
    main()
