"""
# 백준
# No. 2530
# Python 3.11.9
# by "nno0obb"
"""

from datetime import datetime, time, timedelta


def main():
    # Input
    A, B, C = map(int, input().split())
    D = int(input())

    # Logic
    E = datetime.combine(datetime.today(), time(hour=A, minute=B, second=C)) + timedelta(seconds=D)

    # Output
    print(E.strftime("%-H %-M %-S"))


if __name__ == "__main__":
    main()
