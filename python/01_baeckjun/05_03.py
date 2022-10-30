import sys
n = int(sys.stdin.readline().rstrip())
all_area= []
sum = 0

for a in range(1, 101):
    area_tr = []
    for b in range(1, 101):
        area_tr.append(1)
    all_area.append(area_tr)

# 색종이 수 사이클
for i in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    
    #색종이 영역 제거
    for v in range(y, y + 10):   
        for h in range(x, x + 10):
            all_area[v][h] = 0
            
#all_area 다 더하기
for a in range(100):
    for b in range(100):
        sum += all_area[a][b]
print(10000 - sum)