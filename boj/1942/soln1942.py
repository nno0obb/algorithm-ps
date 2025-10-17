"""
# 백준
# No. 1942
# Python 3.11.9
# by "nno0obb"
"""

from datetime import datetime, timedelta


def main():
    # Input
    for _ in range(3):
        start, end = input().split()

        # Logic
        start = datetime.strptime(start, "%H:%M:%S")
        end = datetime.strptime(end, "%H:%M:%S")

        if start > end:
            end += timedelta(days=1)

        ans, curr = 0, start
        while curr <= end:
            num = int(curr.strftime("%H%M%S"))
            if num % 3 == 0:
                ans += 1
            curr += timedelta(seconds=1)

        # Output
        print(ans)


if __name__ == "__main__":
    main()
