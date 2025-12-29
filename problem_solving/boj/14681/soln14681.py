"""
# 백준
# No. 14681 
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    x = int(input())
    y = int(input())

    # Logic
    ans = -1
    if x > 0 and y > 0:
        ans = 1
    elif x < 0 and y > 0:
        ans = 2
    elif x < 0 and y < 0:
        ans = 3
    elif x > 0 and y < 0:
        ans = 4

    # Output
    print(ans)


if __name__ == "__main__":
    main()
