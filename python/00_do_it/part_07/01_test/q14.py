s = input()
result=""
n = 1
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        n += 1
    elif s[i] != s[i+1] or i == len(s)-1:
        result += s[i]+str(n)
        n = 1        
print(result)
