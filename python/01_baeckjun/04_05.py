import sys
stus=list(range(1, 31))
for i in range(0, 28):
    n = int(sys.stdin.readline().rstrip())
    ind=stus.remove(n)

print(min(stus))
print(max(stus))