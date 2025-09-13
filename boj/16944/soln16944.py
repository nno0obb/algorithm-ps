"""
# 백준
# No. 16944
# Python 3.11.9
# by "nno0obb"
"""

import re


def main():
    # Input
    N = int(input())
    S = input()

    # Logic
    cnt = 0
    if not re.sub(r"[^0-9]", "", S):
        cnt += 1
    if not re.sub(r"[^a-z]", "", S):
        cnt += 1
    if not re.sub(r"[^A-Z]", "", S):
        cnt += 1
    if not re.sub(r"[^!@#$%^&*()-+]", "", S):
        cnt += 1
    if N + cnt <= 6:
        cnt = 6 - N

    # Output
    print(cnt)


if __name__ == "__main__":
    main()
