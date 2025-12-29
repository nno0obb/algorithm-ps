"""
# 백준
# No. 1622
# Python 3.11.9
# by "nno0obb"
"""

from collections import Counter


def main():
    # Input
    while True:
        try:
            a = input().strip()
            b = input().strip()

            # Logic
            counter_a, counter_b = Counter(a), Counter(b)
            ans = Counter()
            for char in set(a) & set(b):
                if char in counter_a and char in counter_b:
                    ans[char] = min(counter_a[char], counter_b[char])
                elif char in counter_a:
                    ans[char] = counter_a[char]
                elif char in counter_b:
                    ans[char] = counter_b[char]

            ans = "".join(sorted(ans.elements()))

            #  Output
            print(ans)

        except EOFError:
            break


if __name__ == "__main__":
    main()
