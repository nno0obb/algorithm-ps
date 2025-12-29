"""
# 백준
# No. 31844
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    S = input()

    # Logic
    robot = S.index("@")
    box = S.index("#")
    want = S.index("!")

    ans = -1
    if robot < box < want:
        ans = want - robot - 1
    elif robot > box > want:
        ans = robot - want - 1

    # Output
    print(ans)


if __name__ == "__main__":
    main()
