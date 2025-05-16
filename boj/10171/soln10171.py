"""
# 백준
# No. 10171 
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input

    # Logic
    cat = "\n".join(
        [
            r"\    /\ ".rstrip(),
            r" )  ( ')",
            r"(  /  )",
            r" \(__)|",
        ]
    )

    # Output
    print(cat)


if __name__ == "__main__":
    main()
