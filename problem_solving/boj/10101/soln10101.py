"""
# 백준
# No. 10101
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    a, b, c = int(input()), int(input()), int(input())

    # Logic
    if a + b + c == 180:
        if a == b == c:
            ans = "Equilateral"
        elif a == b or b == c or c == a:
            ans = "Isosceles"
        else:
            ans = "Scalene"
    else:
        ans = "Error"

    # Output
    print(ans)


if __name__ == "__main__":
    main()
