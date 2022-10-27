#예외처리
try:
    a= 1
    b = 0
    print(a / b)
except ZeroDivisionError as e:
    print(e)

try:
    a = [1,2,3]
    print(a[4])
except IndexError as e:
    print(e)