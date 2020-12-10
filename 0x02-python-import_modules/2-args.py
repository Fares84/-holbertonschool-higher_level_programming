#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("1 arguments.")
    else:
        print("{} arguments:".format(len(argv)-1)
