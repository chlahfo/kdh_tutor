#filter()-첫번째는 함수 이름 두번째는 반복 가능한 자료형 -> 두번째 자료형 요소가 첫번째 함수에 입력됐을 때 참인ㄱ섯만 돌려줌.
def positive(l):
    result =[]
    for i in l :
        if i > 0:
            result.append(i)
    return result
print(positive([1, -3, 2, 0, -5, 6]))

#--> filter 로 바꾸기
def positive2(x):
    return x > 0
print(list(filter(positive2, [1, -3, 2, 0, -5, 6])))

print(list(filter(lambda x: x > 0, [1,-3, 2, 0, -5, 6])))

#hex(x)정수 값을 입력받아 16진수로 변환하여 돌려주는 함수
print(hex(234))
print(hex(3))

#id --> 객체를 입력받아 객체의 고유 주소값(레퍼런스)을 돌려주는 함수이다.
a = 3
b = a
print(id(3))
print(id(a))
print(id(b))
print(id(4))

#input--> 사용자의 입력을 받는 함수
a = input()
print(a)
b = input("Enter:")
print(b)

#int --> 문자열 형태의 숫자나 소수점이 있는 숫자등을 정수 형태로 돌려주는 함수.
print(int("3") + int(3.4))

#int("11",진수값 (기본 10))-> 진수값에 따라 앞의 수를 10진수로 변환하여 돌려줌
print(int("11", 2))
print(int("1A", 16))

#isinstance-> 첫번째 인수로 인스턴스 두번째 인수로 클래스 이름을 받는다. 인스턴스가 그 클래스의 인스턴스인지 판단하여 참이면 True, 거짓이면 False 를 돌려준다.
class Person: pass

a=Person()
print(isinstance(a, Person))
b= 3
print(isinstance(b, Person))
