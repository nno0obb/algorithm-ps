"""
# 백준
# No. 2920
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    notes = list(map(int, input().split()))

    # Logic
    order = "mixed"
    if notes == sorted(notes):
        order = "ascending"
    elif notes == sorted(notes, reverse=True):
        order = "descending"

    # Output
    print(order)


if __name__ == "__main__":
    main()
