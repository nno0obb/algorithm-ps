"""
# 백준
# No. 10699 
# Python 3.11.9
# by "nno0obb"
"""

from datetime import datetime, timedelta, timezone


def main():
    # Input

    # Logic
    KST = timezone(timedelta(hours=9))
    seoul_date = datetime.now(KST).strftime("%Y-%m-%d")

    # Output
    print(seoul_date)


if __name__ == "__main__":
    main()
