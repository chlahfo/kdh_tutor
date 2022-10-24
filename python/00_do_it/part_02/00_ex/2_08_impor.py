#format 함수를 이용한 포매팅

#숫자 바로 대입
print("I eat {0} apples".format(3))

# 문자열 바로 대입
print("I eat {0} apples".format("five"))

#숫자를 가진 변수로 대입
num = 3
print("I eat {0} apples".format(num))

#2개 이상의 값 넣기
num = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days." .format(num, day))

#이름으로 넣기 ★
print("I ate {number} apples. so I was sick for {day} days" .format(number=10, day=3))

#인덱스와 이름을 혼용해서 넣기
print("I ate {0} apples. so I was sick for {days}".format(10, days=3))

#왼쪽 정렬 ★
print("{0:<10}".format("hi"))#:<10표현식을 사용하면 치환되는 문자열을 왼쪽으로 정렬하고 문자열 총 자릿수를 10으로 맞출 수 있다. 

#가운데 정렬 ★
print("{0:^10}".format("hi"))#:^10표현식을 사용하면 치환되는 문자열을 가운데로 정렬하고 문자열 총 자릿수를 10으로 맞출 수 있다. 

#오른쪽 정렬 ★
print("{0:>10}".format("hi"))#:<10표현식을 사용하면 치환되는 문자열을 오른쪽으로 정렬하고 문자열 총 자릿수를 10으로 맞출 수 있다. 

#공백 채우기 ★
print("{0:=^10}".format("hi"))#공백 문자 대신 지정한 문자값으로 채우기. 채워넣을 문자는 정렬문자 < > ^ 바로 앞에 넣어야함.
print("{0:!<20}".format("생각보다 책보는데 오래걸림.."))

#소숫점 표현 ★
y = 3.123476789
print("{0:0.4f}".format(y))#소숫점을 3자리까지만 표현 이떄 해당 자릿수는 반올림 처리됨.
print("{0:10.4f}".format(y))#자릿수를 10까지 추가 표현

#{또는}문자 표현하기 ★
print("{{and}}".format())#format 함수를 사용해 문자열 포매팅을 할 경우 {}와 같은 중괄호 문자를 포매팅 문자가 아닌 문자 그대로 사용하고 싶은 경우에는 위 예의 {{}}처럼 2개를 연속해서 사용하면 된다.

#f 문자열 포매팅 (파이썬 3.6 버전 이상만 사용할 수 있는 기능
name="홍길동"
age=30
print(f"나의 이름은 {name}입니다. 나이는 {age}입니다.")#변수 값을 생성한 뒤 그 값을 참조할 수 있음.
print(f"내년이면 나이는 {age}가 됨.")#또한 문자열 포매팅은 표현식을 지원하기 때문에 이런것도 가능
# ★ 표현식이란 문자열 안에서 변수와 +,- 같은 수식을 함께 사용하는 것을 말한다.


#딕셔너리는 f 문자열 포매팅에서 다음과 같이 사용할 수 있다.★
d={"name":"홍길동", "age":30}
print(f"나의 이름은 {d['name']}입니다 나이는 {d['age']}입니다.")

#정렬★
print(f"{'hi':<10}")
print(f"{'hi':>10}")
print(f"{'hi':^10}")

#공백채우기★
print(f"{'hi':~^10}")
print(f"{'hi':!<10}")

#소수점채우기
y=3.42134234
print(f"{y:0.4f}")
print(f"{y:10.4f}")

#문자열에서 {}문자 표시
print(f"{{and}}")  