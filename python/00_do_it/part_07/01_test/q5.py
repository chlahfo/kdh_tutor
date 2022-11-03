import sys
p = [0, 1]
i = 0
n = int(sys.stdin.readline().rstrip())

while True:
    if i >= 2 and p[-1] <= n:
        p.append(p[i-2]+p[i-1])
        
        if p[-1] > n:
            p.pop()
            print(", ".join(map(str,p)))
            break

    i += 1
    
    