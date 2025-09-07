"""
# 백준
# No. 4796
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    i = 1
    while True:
        L, P, V = map(int, input().split())
        if L == 0 and P == 0 and V == 0:
            break

        # Logic
        ans = 0
        ans += (V // P) * L
        ans += min(V % P, L)

        # Output
        print(f"Case {i}: {ans}")
        i += 1


if __name__ == "__main__":
    main()
