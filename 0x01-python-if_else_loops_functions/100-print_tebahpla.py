#!/usr/bin/python3

for i in range(ord('z'), ord('a') - 1, -1):
    print("{0}{1}".format(chr(i), chr(i - 32)), end='')

print()
