"""
# 백준
# No. 31403
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    A = input()
    B = input()
    C = input()

    # Logic
    ans1 = int(A) + int(B) - int(C)
    ans2 = int(A + B) - int(C)

    # Output
    print(ans1)
    print(ans2)


if __name__ == "__main__":
    main()
