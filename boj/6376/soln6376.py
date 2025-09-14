"""
# 백준
# No. 6376
# Python 3.11.9
# by "nno0obb"
"""

from math import factorial


def main():
    # Logic
    E = []
    for n in range(10):
        e = 0
        for k in range(n + 1):
            e += 1 / factorial(k)
        E.append(e)

    # Output
    print("n e")
    print("- -----------")
    for n, e in enumerate(E):
        match n:
            case 0:
                print(f"{n} {int(e)}")
            case 1:
                print(f"{n} {int(e)}")
            case 2:
                print(f"{n} {e:.1f}")
            case _:
                print(f"{n} {e:.9f}")


if __name__ == "__main__":
    main()
