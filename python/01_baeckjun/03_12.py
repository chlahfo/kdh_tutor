#for 12
import sys
n = sys.stdin.readline().rstrip()
if len(n)==1:
    n="0"+n
a = n
x = ""
try_num = 0
while n != x:
    if len(a)==1:
        a="0"+a
    x = a[-1] + str(int(a[0])+int(a[1]))[-1]
    try_num += 1
    a = x
print(try_num)

#for 12 -간결하게 ??
import sys
n = sys.stdin.readline().rstrip()#처음 수
if len(n)==1:
    n="0"+n
a = n #새로운 수
try_num = 0
while n != a or try_num == 0:
    if len(a)==1:
        a="0"+a
    a = a[-1] + str(int(a[0])+int(a[1]))[-1]
    try_num += 1
print(try_num)