import sys

set_s = []
for i in range(10):
    x = int(sys.stdin.readline().rstrip())
    set_s.append(int(x%42))

set_s = set(set_s)
print(len(set_s))
