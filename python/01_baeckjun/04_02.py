# 기존 방식
"""
import sys
n, x = map(int, sys.stdin.readline().rstrip().split())
list_n = list(map(int, sys.stdin.readline().rstrip().split()))
frame = []

for i in range(0, n):
    if list_n[i] < x:
        frame.append(list_n[i])
frame = map(str, frame)

print(" ".join(frame))
"""

#filter와 lambda 썼을 경우
import sys
n, x = map(int, sys.stdin.readline().rstrip().split())
list_n = list(map(int, sys.stdin.readline().rstrip().split()))

if n == len(list_n):
    list_n = list(map(str, filter(lambda item: item < x, list_n)))
    print(" ".join(list_n))