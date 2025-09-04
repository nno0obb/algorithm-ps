"""
# 백준
# No. 15059
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    Ca, Ba, Pa = map(int, input().split())
    Cr, Br, Pr = map(int, input().split())

    # Logic
    ans = 0
    ans += max(0, Cr - Ca)
    ans += max(0, Br - Ba)
    ans += max(0, Pr - Pa)

    # Output
    print(ans)


if __name__ == "__main__":
    main()
