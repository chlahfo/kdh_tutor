#for-7
import sys
t = int(sys.stdin.readline().rstrip())
for i in range(0, t): 
    a,b = map(int, sys.stdin.readline().rstrip().split())
    print("Case #{}: {} + {} = {}".format(i+1, a, b, a+b))