import sys
n = int(sys.stdin.readline().rstrip())
a = sys.stdin.readline().rstrip()
sum = 0
for i in range(len(a)):
    sum += int(a[i])
    
print(sum)