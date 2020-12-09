#!/usr/bin/python3
for nb in range(0, 90):
    if nb == 89:
        print("{:d}".format(nb))
    else:
        if nb / 10 < nb % 10:
            print("{:02d}".format(nb), end=', ')
