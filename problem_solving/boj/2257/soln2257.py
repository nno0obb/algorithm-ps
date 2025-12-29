"""
# 백준
# No. 2257 
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    F = input()

    # Logic
    stack = []
    for c in F:
        if c in ["H", "C", "O"]:
            stack.append(
                {
                    "H": 1,
                    "C": 12,
                    "O": 16,
                }[c]
            )
        elif c == "(":
            val = 0
            while stack and stack[-1] != "(":
                val += stack.pop()
            stack.append(val)
            stack.append("(")
        elif c == ")":
            val = 0
            while stack and stack[-1] != "(":
                val += stack.pop()
            stack.pop()
            stack.append(val)
        elif c in "23456789":
            stack[-1] *= int(c)
        else:
            raise RuntimeError()

    ans = sum(stack)

    # Output
    print(ans)


if __name__ == "__main__":
    main()
