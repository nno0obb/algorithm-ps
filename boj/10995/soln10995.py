"""
# 백준
# No. 10995
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())

    # Logic
    ans = ""
    for i in range(N):
        line = (" *" * N).strip()
        if i % 2:
            line = " " + line
        ans += line + "\n"

    # Output
    print(ans)


if __name__ == "__main__":
    main()
