"""
# 백준
# No. 3460
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    T = int(input())
    for _ in range(T):
        N = int(input())

        # Logic
        indicies = []
        for idx, bit in enumerate(bin(N)[2:][::-1]):
            if bit == "1":
                indicies.append(idx)

        # Output
        print(*indicies, sep=" ")


if __name__ == "__main__":
    main()
