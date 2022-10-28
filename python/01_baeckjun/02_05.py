#if-5
h, m = map(int, input().split())
if m < 45:
    h, m = h-1, m+60
    if h < 0:
        h = h+24
    print(h, m-45)
else:
    print(h, m-45)