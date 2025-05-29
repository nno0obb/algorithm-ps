"""
# 백준
# No. 2744 
# Python 3.11.9
# by "nno0obb"
"""


def switch(c: str):
    if c.isupper():
        return c.lower()
    elif c.islower():
        return c.upper()
    raise RuntimeError()


def main():
    # Input
    s = input()

    # Logic
    ans = "".join(switch(c) for c in s)

    # Output
    print(ans)


if __name__ == "__main__":
    main()
