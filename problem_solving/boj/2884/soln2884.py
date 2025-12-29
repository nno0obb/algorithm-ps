"""
# 백준
# No. 2884
# Python 3.11.9
# by "nno0obb"
"""

from datetime import datetime, timedelta


def main():
    # Input
    H, M = map(int, input().split())

    # Logic
    alarm = datetime.now().replace(hour=H, minute=M, second=0, microsecond=0)
    early = (alarm - timedelta(minutes=45)).time()

    # Output
    print(early.strftime("%-H %-M"))


if __name__ == "__main__":
    main()
