#if -7
a, b, c = map(int, input().split())
if a == b and b == c:
    print(a*1000+10000)
elif a == b or b == c:
    print(b*100+1000)
elif a == c:
    print(a*100+1000)
else: 
    if a > b and a > c: print(a*100)
    if b > a and b > c : print(b*100)
    if c > a and c > b : print(c*100)