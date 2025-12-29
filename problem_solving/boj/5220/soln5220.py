"""
# 백준
# No. 5220
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    T = int(input())
    for _ in range(T):
        num, check_bit = map(int, input().split())

        # Logic
        ans = "Valid" if num.bit_count() % 2 == check_bit else "Corrupt"

        # Output
        print(ans)


if __name__ == "__main__":
    main()
