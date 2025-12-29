"""
# 백준
# No. 13623 
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    A, B, C = map(int, input().split())

    # Logic
    ans = "*"
    bits = int(f"0b{A}{B}{C}", 2)
    if bits == 0b100 or bits == 0b011:
        ans = "A"
    elif bits == 0b010 or bits == 0b101:
        ans = "B"
    elif bits == 0b001 or bits == 0b110:
        ans = "C"

    # Output
    print(ans)


if __name__ == "__main__":
    main()
