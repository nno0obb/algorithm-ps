"""
# 백준
# No. 2675
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    T = int(input())
    for _ in range(T):
        R, S = input().split()

        # Logic
        ans = "".join(map(lambda x: x * int(R), list(S)))

        # Output
        print(ans)


if __name__ == "__main__":
    main()
