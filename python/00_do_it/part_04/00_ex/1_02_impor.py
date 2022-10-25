#매개변수 지정하여 호출하기
import re


def add(a, b):
    return a - b

aa=result=add(a=3, b=7)
bb=result=add(b=7, a=3)# 순서 상관없이 쓸 수 있음.

print(aa, bb)

#입력값이 몇 개가 될지 모를 때
def add_many(*args): # 매개변수 앞에 *를 붙이면 입력값을 전부 모아서 튜플로 만들어준다. arg 는 단순 이름으로 변경 가능하다.
    result = 0
    for i in args:
        result += i
    return result

print(add_many(1,2,4,6,3,7,7))

# 다른 변수와 혼용해서 사용할 때
def add_mul(choice, *args_list):
    if choice =="add":
        result = 0
        for i in args_list:
            result += i
    elif choice == "mul":
        result = 1
        for i in args_list:
            result *= i
    else:
        print("흠..")
    return result

result=add_mul("add", 1,2,3,4)
print(result)
result= add_mul("mul", 1,2,3,4)
print(result)

#키워드 파라미터
def print_kwargs(**kwargs):#앞에 별 두개
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name = "foo", age = 3)
#매개 변수 앞에 **를 붙이면 매개변수 kwarg는 딕셔너리가 되고, 모든 key=value 형태의 결괏값이 그 딕셔너리에 저장된다.
