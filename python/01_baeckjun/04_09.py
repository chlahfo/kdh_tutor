# round 함수...
import sys
c = int(sys.stdin.readline().rstrip())

for i in range(c):
    n = list(map(int, sys.stdin.readline().rstrip().split()))
    
    if n[0] == len(n)-1 and n[0] != 0:
        sums = sum(n[1:])
        balance = sums / n[0]
        n_pic = len(list(filter(lambda x: x > balance, n[1:])))
        total = n_pic / n[0] * 100
        print("{:.3f}%" .format(total))
        
    elif n[0] == 0:
        print("{:.3f}%" .format(0))
        
    else:
        pass