"""
# 백준
# No. 24087
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    S = int(input())
    A = int(input())
    B = int(input())

    # Logic
    height, cost = A, 250
    if S > height:
        diff = S - height
        cost += (diff + B - 1) // B * 100

    # Output
    print(cost)


if __name__ == "__main__":
    main()
