#계산기 덧셈
"""
result1 = 0
result2 = 0
def add(num):
    global result1
    result1 +=num
    return result1

def add2(num):
    global result2
    result2 +=num
    return result2
print(add(3))
print(add(4))
print(add2(3))
print(add2(7))
"""
sum = 0
def add(num, result):
    result = result + num
    return result
sum = add(3, sum)
print(sum)
sum = add(4, sum)
print(sum)
