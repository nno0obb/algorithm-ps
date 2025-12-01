"""
# 백준
# No. 2018
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())

    # Logic
    ans, i = 0, 1
    while True:
        offset = i * (i + 1) // 2
        if offset <= N and (N - offset) % i == 0:
            ans += 1
        elif offset > N:
            break
        i += 1

    # Output
    print(ans)

    # Hint
    # 1+1n
    # 3+2n
    # 6+3n
    # 10+4n
    # 15+5n
    # 21+6n
    # ...


if __name__ == "__main__":
    main()
