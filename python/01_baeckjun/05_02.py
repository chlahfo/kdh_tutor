import sys
table = []
max_s = []
tr_n = 0
td_n = 0

for i in range(9):
    tr = list(map(int, sys.stdin.readline().rstrip().split()))
    table.append(tr)
    max_s.append(max(tr))
    

best_max = max(max_s)
tr_n = max_s.index(best_max)
td_n = table[tr_n].index(best_max)
print(best_max)
print(tr_n + 1, td_n + 1)