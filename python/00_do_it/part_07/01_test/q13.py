"""
s = list(input())
result = []

if s:
    result.append(s[0])
    for i in range(len(s)-1):

        if int(s[i]) % 2 == 0 and int(s[i+1]) % 2 == 0:
            result.append("*")
        elif int(s[i]) % 2 == 1 and int(s[i+1]) % 2 == 1:
            result.append("-")
        else:
            pass
        result.append(s[i+1])
print("".join(result))
"""

#
def DashInsert(aaa):
    s=list(aaa)
    result=[]

    if s:
        result.append(s[0])
        for i in range(len(s)-1):

            if int(s[i]) % 2 == 0 and int(s[i+1]) % 2 == 0:
                result.append("*")
            elif int(s[i]) % 2 == 1 and int(s[i+1]) % 2 == 1:
                result.append("-")
            else:
                pass
            result.append(s[i+1])
    result = "".join(result)

    return result
print(DashInsert(input()))