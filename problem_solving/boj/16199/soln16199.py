"""
# 백준
# No. 16199
# Python 3.11.9
# by "nno0obb"
"""

from datetime import datetime


def main():
    # Input
    birth_year, birth_month, birth_day = map(int, input().split())
    today_year, today_month, today_day = map(int, input().split())

    # Logic
    birth_date = datetime(year=birth_year, month=birth_month, day=birth_day)
    today_date = datetime(year=today_year, month=today_month, day=today_day)

    year_age = today_date.year - birth_date.year
    kor_age = year_age + 1
    std_age = year_age if (today_date.month, today_date.day) >= (birth_date.month, birth_date.day) else year_age - 1

    # Output
    print(std_age)
    print(kor_age)
    print(year_age)


if __name__ == "__main__":
    main()
