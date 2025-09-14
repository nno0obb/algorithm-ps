"""
# 백준
# No. 4999
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    jaehwan = input()
    doctor = input()

    # Logic
    ans = "go" if len(jaehwan) >= len(doctor) else "no"

    # Output
    print(ans)


if __name__ == "__main__":
    main()
