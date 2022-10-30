import sys
s = sys.stdin.readline().rstrip()
alpab = []
result = []
for i in range(97, 123):
    alpab.append(chr(i))

for j in range(len(alpab)):
    count = 0
    if alpab[j] in s:
        count = s.index(alpab[j])
    else:
        count = -1
    result.append(count)

print(" ".join(map(str, result)))