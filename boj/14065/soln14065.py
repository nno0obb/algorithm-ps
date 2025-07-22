"""
# 백준
# No. 14065
# Python 3.11.9 (PyPy3..?)
# by "nno0obb"
"""


def main():
    # Input
    x = float(input())

    # Logic
    # x (mile/gallon)
    # x ((1.609344 * km) / (3.785411784 * L))
    # (x * 1.609344) / 3.785411784 (km/L)
    # (x * 1.609344) / (3.785411784 * 100) (100km/L)
    # (3.785411784 * 100) / (x * 1.609344) (L/100km)
    ans = (3.785411784 * 100) / (x * 1.609344)

    # Output
    print(ans)


if __name__ == "__main__":
    main()
