"""
# 백준
# No. 31520
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = input()

    # Logic
    num, idx, ans, flag = 1, 0, -1, True
    while True:
        for j in str(num):
            if not idx < len(N) or j != N[idx]:
                flag = False
                break
            idx += 1

        if not flag:
            break

        ans = num
        num += 1

        if idx == len(N):
            break

    if not flag:
        ans = -1

    # Output
    print(ans)


if __name__ == "__main__":
    main()
