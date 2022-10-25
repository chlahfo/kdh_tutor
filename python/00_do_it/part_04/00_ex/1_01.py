#함수 기본(dlfqksgkatndml wjsgudwjrdls dP)
def add(a, b):
    return a+b
a = 3
b = 4
c= add(a, b)
print(c)

print(add(a, b))

#입력값이 없는 함수
def say():
    return "Hi"
a= say()
print(a)

#결과값이 없는 함수
def add(a, b):
    print("%d , %d의 합은 %d 입니다." %(a, b, a+b))

add(3,4)

#입력값도 결괏값도 없는 함수.
def say():
    print("Hi")

say()