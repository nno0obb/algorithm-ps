"""
# 백준
# No. 2869
# Python 3.11.11
# by "nno0obb"
"""


def main():
    # Input
    A, B, V = map(int, input().split())

    # Logic
    ## daily_len = A - B
    ## last_day = 1
    ## until_last_len = V - A
    ## until_last_day = (until_last_len + (daily_len - 1)) // daily_len
    ## ans = until_last_day + last_day
    ans = ((V - A) + (A - B - 1)) // (A - B) + 1

    # Output
    print(ans)


if __name__ == "__main__":
    main()
