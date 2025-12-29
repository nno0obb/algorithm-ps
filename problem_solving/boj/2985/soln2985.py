"""
# 백준
# No. 2985
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    A, B, C = map(int, input().split())

    # Logic
    ans = ""
    match C:
        case C if A + B == C:
            ans = f"{A}+{B}={C}"
        case C if A - B == C:
            ans = f"{A}-{B}={C}"
        case C if A * B == C:
            ans = f"{A}*{B}={C}"
        case C if A / B == C:
            ans = f"{A}/{B}={C}"

    match A:
        case A if A == B + C:
            ans = f"{A}={B}+{C}"
        case A if A == B - C:
            ans = f"{A}={B}-{C}"
        case A if A == B * C:
            ans = f"{A}={B}*{C}"
        case A if A == B / C:
            ans = f"{A}={B}/{C}"

    # Output
    print(ans)


if __name__ == "__main__":
    main()
