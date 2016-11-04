#!/usr/bin/python

count = 0
while count < 5:
    print count, "a"
    if (count == 3):
        break
    count += 1
else:
    print count