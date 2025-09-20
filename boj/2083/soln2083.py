"""
# 백준
# No. 2083
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    while True:
        name, age, weight = input().split()
        if (name, age, weight) == ("#", "0", "0"):
            break

        # Logic
        is_senior = (int(age) > 17) or (int(weight) >= 80)

        # Output
        print(name, "Senior" if is_senior else "Junior")


if __name__ == "__main__":
    main()
