#!/usr/bin/python3
r = 0
for i in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(i - r)), end="")
    r = 32 if r == 0 else 0
