"""
# 백준
# No. 16561
# Python 3.11.9
# by "nno0obb"
"""

# Global Variables
MAX_N = 1000


def main():
    # Input
    N = int(input())

    # Logic
    N //= 3
    ans = (N - 1) * (N - 2) // 2  # x|x|x|x|x|x|x (N=21, 6C2)

    # Output
    print(ans)


if __name__ == "__main__":
    main()
