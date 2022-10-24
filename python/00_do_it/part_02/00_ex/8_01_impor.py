#변수
a=1
b="python"
c=[1,2,3]
#자료형 지정 안해도 됨.
#[1,2,3]이 메모리에 생성되고, c는 메모리 주소를 가르킴

#메모리 주소는 다음과 같이 확인 가능
print(id(c))
#id() : 변수가 가르키고 있는 객체의 주소값을 돌려주는 파이썬 내장함수.

#리스트 복사
a=[1,2,3]
b=a
print(id(a))
print(id(b))
#b는 a와 완전 동일해짐. 리스트를 참조하는 변수 a 에서 b변수가 추가되었을 뿐.

print(a is b)


a[1] =4
print(a)
print(b)
#a 나 b 둘 중 하나를 바꾸면 둘 다 바뀜

#질문: 왜 a 가 안들어가지지
a = 5
b = a
print(id(a))
print(id(b))
b = b + 1
print(a , b)
print(id(a))
print(id(b))
#왜 리스트 조작 함수에서 적용한 것은 값이 똑같이 적용되는데 변수에서 단순한 사직연산은 따로 가는건지..id 의 값은 같은데..?
#사칙연산을 하는 순간에 id 값이 바뀐다...?!

m=[1,2,3]
n=m
n=n + [4, 5]
print(m, n)

n = 1
print(id(n))
n = 2
print(id(n))

#재 할당하는 순간에 메모리 주소 값이 바뀌나봄..그래서 따로 놀게 되는거..