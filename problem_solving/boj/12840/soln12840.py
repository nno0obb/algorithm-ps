"""
# 백준
# No. 12840
# Python 3.11.9
# by "nno0obb"
"""

from datetime import datetime, time, timedelta


def main():
    # Input
    h, m, s = map(int, input().split())
    Q = [list(map(int, input().split())) for _ in range(int(input()))]

    # Logic
    now = datetime.combine(datetime.today(), time(hour=h, minute=m, second=s))
    for q in Q:
        T, *c = q
        if T == 1:
            now += timedelta(seconds=c[0])
        elif T == 2:
            now -= timedelta(seconds=c[0])

        # Output
        elif T == 3:
            print(now.strftime("%-H %-M %-S"))


if __name__ == "__main__":
    main()
