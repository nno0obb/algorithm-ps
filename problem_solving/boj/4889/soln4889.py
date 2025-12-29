"""
# 백준
# No. 4889
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    test_case = 0
    while True:
        S = input()
        if "-" in S:
            break

        # Logic
        test_case += 1
        stack = []
        for c in S:
            if c == "{":
                stack.append(c)
            elif c == "}":
                if stack and stack[-1] == "{":
                    stack.pop()
                    continue
                stack.append(c)

        ans = 0
        for i, c in enumerate(stack):
            if c == "{" and i % 2 == 0:
                continue
            elif c == "}" and i % 2 == 1:
                continue
            ans += 1

        # Output
        print(f"{test_case}. {ans}")


if __name__ == "__main__":
    main()
