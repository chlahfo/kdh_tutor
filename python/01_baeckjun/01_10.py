
a = [1, 1, 2, 2, 2, 8]
b = list(map(int, input().split()))
num = 0

for i in a:
    print(a[num]- b[num], end=" ")
    num+=1