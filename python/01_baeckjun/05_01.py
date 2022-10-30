import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
a = []
b = []
result = []
for i in range(n):
    a.append(list(map(int, sys.stdin.readline().rstrip().split())))
    
for i in range(n):
    b.append(list(map(int, sys.stdin.readline().rstrip().split()))) 

for i in range(n):
    result_item = []
    for j in range(m):
        result_item.append(a[i][j] + b[i][j])
        
    print(" ".join(map(str, result_item)))