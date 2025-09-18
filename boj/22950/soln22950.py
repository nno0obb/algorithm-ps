"""
# 백준
# No. 22950
# Python 3.11.9
# by "nno0obb"
"""

import ast


def main():
    # Input
    N = int(input())
    M = input()
    K = int(input())

    # Logic
    M = ast.literal_eval("0b" + M)

    # Output
    if M % (1 << K):
        print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    main()
