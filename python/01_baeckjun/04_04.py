import sys
list_m = []

for i in range(0, 9):
    x = sys.stdin.readline().rstrip()
    list_m.append(int(x))

list_max = max(list_m)
print(list_max)
print(list_m.index(list_max)+1)