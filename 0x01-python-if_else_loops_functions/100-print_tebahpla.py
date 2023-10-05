#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    case = chr(i - 32) if i % 2 == 0 else chr(i)
    print(case, end="")
