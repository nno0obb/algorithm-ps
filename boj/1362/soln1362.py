"""
# 백준
# No. 1362
# Python 3.11.9
# by "nno0obb"
"""


def main():
    # Input
    senario = 0
    while True:
        O, W = map(int, input().split())
        if (O, W) == (0, 0):
            break

        senario += 1
        status = "alive"
        while True:
            cmd, val = input().split()

            # Logic
            if (cmd, status) == ("E", "alive"):
                W -= int(val)
                if W <= 0:
                    status = "dead"
            elif (cmd, status) == ("F", "alive"):
                W += int(val)
            elif cmd == "#":

                # Output
                if status == "dead":
                    status = "RIP"
                elif (O / 2) < W < (O * 2):
                    status = ":-)"
                else:
                    status = ":-("

                # Output
                print(f"{senario} {status}")
                break


if __name__ == "__main__":
    main()
