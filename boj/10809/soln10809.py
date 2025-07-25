"""
# 백준
# No. 10809
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    S = input()

    # Logic, Ouptut
    for i in range(ord("a"), ord("z") + 1):
        print(S.find(chr(i)), end=" ")


if __name__ == "__main__":
    main()
