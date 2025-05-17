"""
# 백준
# No. 2753 
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    year = int(input())

    # Logic
    is_leap = False
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            is_leap = True

    # Output
    print(1 if is_leap else 0)


if __name__ == "__main__":
    main()
