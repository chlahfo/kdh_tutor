#문자열 압축하기
import sys
import re
st = sys.stdin.readline().rstrip()
result=""
count=1

for i in range(len(st)):
    if i+1 != len(st):
        if st[i] == st[i+1]:
            count += 1
        else:
            result += st[i] + str(count)
            count = 1
    else:
        result += st[i] + str(count)
        count = 1
print(result)