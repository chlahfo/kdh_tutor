import sys
n = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

if n == len(nums):
    min_n = int(min(nums))
    max_n = int(max(nums))
    print(min_n, max_n)
