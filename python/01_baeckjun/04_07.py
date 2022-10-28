import sys
n = int(sys.stdin.readline().strip())
score_list = list(map(int, sys.stdin.readline().split()))
m = max(score_list)
sum = 0

for i in range(0, n):
    sum += score_list[i] / m * 100

print(sum / n)