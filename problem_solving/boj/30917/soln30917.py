"""
# 백준
# No. 30917
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    A, B = -1, -1
    for char in "AB":
        for i in range(9):
            print(f"? {char} {i + 1}", flush=True)

            resp = int(input())

            # Logic
            if resp == 1:
                if char == "A":
                    A = i + 1
                    break
                elif char == "B":
                    B = i + 1
                    break

    # Output
    print(f"! {A+B}")


if __name__ == "__main__":
    main()
