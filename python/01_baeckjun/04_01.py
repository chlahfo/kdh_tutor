
# count  함수 이용
import sys
#sys.stdin.readline().rstrip()

n = int(sys.stdin.readline().rstrip())
all_nums = list(map(int, sys.stdin.readline().rstrip().split()))
v = int(sys.stdin.readline().rstrip())
print(all_nums.count(v))

""" 
# 원래 출제 의도같은 것?(n 이용)
import sys
n = int(sys.stdin.readline().rstrip())
all_nums = list(map(int, sys.stdin.readline().rstrip().split()))
v = int(sys.stdin.readline().rstrip())
count_n = 0

for i in range(0, n):
    if v == all_nums[i]:
        count_n += 1
    

print(count_n)
"""