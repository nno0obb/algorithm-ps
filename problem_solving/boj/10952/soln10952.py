"""
# 백준
# No. 10952 
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
        ans = A + B

        # Output
        print(ans)


if __name__ == "__main__":
    main()
