"""
# 백준
# No. 1874
# Python 3.11.9
# by "nno0obb"
"""

import sys


def main():
    # Input
    n = int(input())
    A = [int(sys.stdin.readline().strip()) for _ in range(n)]

    # Logic
    cmds, stack, max_num, is_possible = [], [], 0, True
    for num in A:
        if num > max_num:
            for i in range(max_num + 1, num + 1):
                stack.append(i)
                cmds.append("+")
            max_num = num
            stack.pop()
            cmds.append("-")
        else:
            if stack and stack[-1] != num:
                is_possible = False
                break
            stack.pop()
            cmds.append("-")

    # Output
    print("\n".join(cmds) if is_possible else "NO")

    # Hint
    # +: [1]
    # +: [1 2]
    # +: [1 2 3]
    # +: [1 2 3 4]
    # -: [1 2 3]     --- 4
    # -: [1 2]       --- 4 3
    # +: [1 2 5]     --- 4 3
    # +: [1 2 5 6]   --- 4 3
    # -: [1 2 5]     --- 4 3 6
    # +: [1 2 5 7]   --- 4 3 6
    # +: [1 2 5 7 8] --- 4 3 6
    # -: [1 2 5 7]   --- 4 3 6 8
    # -: [1 2 5]     --- 4 3 6 8 7
    # -: [1 2]       --- 4 3 6 8 7 5
    # -: [1]         --- 4 3 6 8 7 5 2
    # -: []          --- 4 3 6 8 7 5 2 1


if __name__ == "__main__":
    main()
