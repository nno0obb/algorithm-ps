"""
# 백준
# No. 1330 
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    A, B = map(int, input().split())

    # Logic
    ans = "=="
    if A < B:
        ans = "<"
    elif A > B:
        ans = ">"

    # Output
    print(ans)


if __name__ == "__main__":
    main()
