import sys
n = int(sys.stdin.readline().rstrip())


for i in range(n):
    s = sys.stdin.readline().rstrip()
    s_n = int(s[0])
    s = s[2:]
    p=""
    
    for j in range(len(s)):
        p += s[j] * s_n
    
    print(p)

