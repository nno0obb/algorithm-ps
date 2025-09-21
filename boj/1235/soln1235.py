"""
# 백준
# No. 1235
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())
    A = [input() for _ in range(N)]

    # Logic
    k = 0
    while True:
        k += 1
        B = [no[-k:] for no in A]
        if len(set(B)) == N:
            break
    ans = k

    # Output
    print(ans)


if __name__ == "__main__":
    main()
