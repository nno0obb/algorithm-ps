"""
# 백준
# No. 23809
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())

    # Logic
    output = []
    s1 = "@" * N + " " * 3 * N + "@" * N
    s2 = "@" * N + " " * 2 * N + "@" * N
    s3 = "@" * N + "@" * 1 * N + "@" * N
    for s in [s1, s2, s3, s2, s1]:
        output.extend([s] * N)

    # Output
    print("\n".join(output))


if __name__ == "__main__":
    main()
