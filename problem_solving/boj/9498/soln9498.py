"""
# 백준
# No. 9498 
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    score = int(input())

    # Logic
    ans = "F"
    if score >= 90:
        ans = "A"
    elif score >= 80:
        ans = "B"
    elif score >= 70:
        ans = "C"
    elif score >= 60:
        ans = "D"

    # Output
    print(ans)


if __name__ == "__main__":
    main()
