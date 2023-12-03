#!/usr/bin/python3
for index1 in range(10):
    for index2 in range(index1 + 1, 10):
        if index1 * 10 + index2 < 89:
            print("{:d}{:d}".format(index1, index2), end=", ")
print("{:d}".format(89))
