"""
# 백준
# No. 28278 
# Python 3.11.9
# by "nno0obb"
"""

import sys


def main():
    # Input
    N = int(input())

    # Logic, Output
    stk = []
    for _ in range(N):
        cmd = sys.stdin.readline().split()
        if cmd[0] == "1":
            stk.append(cmd[1])
        elif cmd[0] == "2":
            if stk:
                print(stk.pop())
            else:
                print(-1)
        elif cmd[0] == "3":
            print(len(stk))
        elif cmd[0] == "4":
            print(1 if not stk else 0)
        elif cmd[0] == "5":
            if stk:
                print(stk[-1])
            else:
                print(-1)


if __name__ == "__main__":
    main()
