"""
# 백준
# No. 25192
# Python 3.11.9
# by "nno0obb"
"""

import sys


def main():
    # Input
    N = int(input())
    logs = [sys.stdin.readline().strip() for _ in range(N)]

    # Logic
    cnt, do_hi = 0, set()
    for log in logs:
        if log == "ENTER":
            do_hi.clear()
        else:
            nickname = log
            if nickname not in do_hi:
                do_hi.add(nickname)
                cnt += 1

    # Output
    print(cnt)


if __name__ == "__main__":
    main()
