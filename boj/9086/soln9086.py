"""
# 백준
# No. 9086 
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    T = int(input())
    for _ in range(T):
        S = input()

        # Logic
        ans = S[0] + S[-1]

        # Output
        print(ans)


if __name__ == "__main__":
    main()
