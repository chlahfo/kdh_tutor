#for-8
import sys
t = int(sys.stdin.readline().rstrip())
for i in range(0, t):
    print("{}{}".format(" "*(t-i-1),"*"*(i+1)))