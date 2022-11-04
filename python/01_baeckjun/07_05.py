import sys
s = (sys.stdin.readline().rstrip()).upper()
alpa_n = []
for i in range(65, 91):
    alpa_n.append(0)

for j in range(len(s)):
    alpa_n[ord(s[j]) - 65] += 1
max_n=max(alpa_n)
max_i=alpa_n.index(max_n)


if alpa_n.count(max_n) == 1:
    print(chr(max_i + 65))
else:
    print("?")
