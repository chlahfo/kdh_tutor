#for-9
import sys
n, x = map(int,sys.stdin.readline().rstrip().split())
nums = list(map(int,sys.stdin.readline().rstrip().split()))
sum = []

for i in range(0, n):
    if nums[i] < x: sum.append(str(nums[i]))
    
if len(sum) != 0:
    print(' '.join(sum))