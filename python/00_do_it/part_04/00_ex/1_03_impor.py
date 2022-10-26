#함수의 결괏값은 언제나 하나
def add_and_mul(a,b):
    return a+b, a*b # 이럴 때 값을 튜플 값으로 돌려주므로 결괏값은 하나이다.
result = add_and_mul(3,4)
print(result)#(7, 12)

#만약, 이 하나의 튜플 값을 2개의 결괏값으로 받고싶다면 다음과 같이 받는다.(튜플 값 할당처럼) ★★★
result1, result2 = add_and_mul(3,4)

print(result1)
print(result2)

#함수는 return 문을 만나는 순간 결괏값을 돌려준다음 함수를 빠져나가게 된다.
#따라서 return 문을 두번 쓰면 처음 return 문이 실행되고 함수가 종료된다.

#return 의 또다른 쓰임새: 특별한 상황일 때 함수를 빠져나가고 싶으면 return 을 단독으로 써서 함수를 즉시 빠져나갈 수 있다.

def say_nick(nick):
    if nick =="바보":
        return
    print("나의 별명은 %s입니다." %nick)
say_nick("야호")
say_nick("바보")

#매개변수에 초깃값 미리 설정하기 - 단 실제로 잘 쓰이진 않음
#초깃값 설정 매개변수 뒤에 일반 매개변수를 둘 수 없음
def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." %name)
    print("나이는 %d 입니다." %old)
    if man:
        print("남자입니다.")
        
    else:
        print("여자입니다.")
say_myself("박응용", 27)
say_myself("박응용", 27, True)
say_myself("박응선", 27, False)

# 함수 효력 범위 
# 매개변수는 함수 안에서만 사용되며 이름 바꿔도 그 안에서 통일하면 상관 x
# 함수 안에서 전역 변수를 바꾸는 문장이 있어도, 함수 바깥에서까지는 적용되지 않음
a= 1
def vartest(b):
    b+=1
vartest(a)
print(a)

#함수 안에서 함수 밖의 변수를 변경하는 방법
#1. return 사용하기 
a = 1
def vartest(b):
    b=b+1
    return b

a = vartest(a)
print(a)

#2. global 명령어 사용 
# 함수 밖의 a 변수를 직접 사용하겠다는 뜻이다.
# 사용하지 않는 것이 좋다. 함수는 독립적으로 존재하는 것이 좋기 때문이다. 외부 변수에 종속적인 함수는 그다지 좋은 함수가 아니다. 첫번쨰 방법이 좋다.
a = 1
def vartest():
    global a
    a += 1
vartest()
print(a)

#lambda 함수를 생성할 때 사용하는 예약어. def 와 동일한 역할. 보통 함수를 한줄로 간결하게 만들 때 사용.(return 명령어가 없어도 결과값을 돌려줌.)★★★
add = lambda a,b : a+b
resulte = add(3,4)
print(result)

#이 함수와 동일
def add(a,b):
    return a+b
resulte = add(3, 4)
print(result)
