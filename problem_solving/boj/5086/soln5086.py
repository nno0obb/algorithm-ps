"""
# 백준
# No. 5086
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    while True:
        A, B = map(int, input().split())
        if A == 0 and B == 0:
            break

        # Logic
        if B % A == 0:
            ans = "factor"
        elif A % B == 0:
            ans = "multiple"
        else:
            ans = "neither"

        # Output
        print(ans)


if __name__ == "__main__":
    main()
