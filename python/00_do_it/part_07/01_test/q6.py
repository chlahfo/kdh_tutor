import sys
s = sys.stdin.readline().rstrip()

if s:
    s=map(int, s.split(","))
    sum_s = sum(s)
    print(sum_s)