import sys
s = sys.stdin.readline().rstrip()
alpa_n = []
for i in range(97, 123):
    alpa_n.append(0)

for j in range(len(s)):
    #아직 소문자만 구현중
    alpa_n[chr(s[j]) - 97] += 1