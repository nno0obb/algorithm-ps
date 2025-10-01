"""
# 백준
# No. 11365
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    codes = []
    while True:
        code = input()
        if code == "END":
            break
        codes.append(code)

    # Logic, Output
    for code in codes:
        print(code[::-1])


if __name__ == "__main__":
    main()
