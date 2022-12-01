#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum = 0
    n = len(argv)
    for count in range(1, n):
        sum += int(argv[count])
    print("{}".format(sum))
