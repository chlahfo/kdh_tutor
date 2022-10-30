list_n = list(range(1, 10001))
import sys
def d(n):
    n = str(n)
    num = int(n)
    
    for i in range(len(n)):
        num += int(n[i])    
    return num
    
for j in range(1, 10001):
    if d(j) in list_n:
        list_n.remove(d(j))
for k in range(len(list_n)):
    print(list_n[k])
