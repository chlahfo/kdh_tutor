import sys
a, b = map(list, sys.stdin.readline().rstrip().split())
a.reverse()
b.reverse()
a = int("".join(a))
b = int("".join(b))
if a - b > 0:
    print(a)
else:
    print(b)