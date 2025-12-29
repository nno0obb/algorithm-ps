"""
# 백준
# No. 20413
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())
    S, G, P, D = map(int, input().split())
    MVPs = input()

    # Logic
    ans, prev, curr = 0, 0, -1
    for mvp in MVPs:
        match mvp:
            case "B":
                curr = max(0, (S - 1) - prev)
            case "S":
                curr = max(0, (G - 1) - prev)
            case "G":
                curr = max(0, (P - 1) - prev)
            case "P":
                curr = max(0, (D - 1) - prev)
            case "D":
                curr = D
            case _:
                raise RuntimeError()
        ans += curr
        prev = curr

    # Output
    print(ans)


if __name__ == "__main__":
    main()
