"""
# 백준
# No. 2929
# Python 3.11.9
# by "nno0obb"
"""

import re


def main():
    # Input
    C = input()

    # Logic
    cmds = re.split("(?=[A-Z])", C)[1:]

    nops = 0
    for cmd in cmds[:-1]:
        if len(cmd) % 4 > 0:
            nops += 4 - (len(cmd) % 4)

    # Output
    print(nops)


if __name__ == "__main__":
    main()
