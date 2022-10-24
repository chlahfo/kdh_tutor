#Pithon -> Python 변경
from tkinter import Y


a="Pithon"
#a[1] = "y" -> 오류 발생. 문자열 요솟값은 바꿀수 있는 값이 아님.그래서 immutable한 자료형이라고도 부름.
b=a[:1]+"y"+a[2:]
print(b)#바꾸려면 이렇게 바꿔야함.

#문자열 포매팅
#숫자 바로 대입
print("I eat %d apples" %3)

#문자열 바로 대입
print("I eat %s apples" %"five")

# 숫자값을 나타내는 변수 대입
num =3
print("I eat %d apples" %num)

#2개 이상의 값 넣기
num =10
day="three"
print("I ate %d apples. so I was sick for %s days." %(num, day))

#문자열 포맷팅 코드 %s(문자열) %c(문자 1개) %d(정수) %f(실수) %o(8진수) %x (16진수) %%(Literal 문자 % 자체)
print("I have %s apples %3")
print("rate is %s" %3.234)
#%s 를 사용하면 자동으로 %뒤에 있는 값을 문자열로 바꿈.

print("Error is %d%%" %98)#포매팅 연산자와 같이 쓰면 %를 %% 로 표시해줘야함. 단, 포매팅 연산자가 없으면 %는 홀로 쓰여도 됨.


