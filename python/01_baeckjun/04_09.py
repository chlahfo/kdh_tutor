import sys
c = int(sys.stdin.readline().rstrip())

for i in range(c):
    n = list(map(int, sys.stdin.readline().rstrip().split()))
    n_pic = 0
    sum = 0
    for j in range(n[0]):
        sum += n[j+1]
    
    #print(sum, n[0], sum / n[0])
    #print(str(round(sum/n[0], 3))+"%")