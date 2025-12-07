"""
# 백준
# No. 25918
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    N = int(input())
    S = input()

    # Logic
    pairs = [tuple("()"), tuple(")(")]
    stack, ans = [], 0
    for c in S:
        if stack and (stack[-1], c) in pairs:
            stack.pop()
        else:
            stack.append(c)

        ans = max(ans, len(stack))

    if stack:
        ans = -1

    # Output
    print(ans)


if __name__ == "__main__":
    main()
