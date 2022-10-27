#내장함수
#abs(x):x의 절댓값 돌려주는 함수
print(abs(3))
print(abs(-12))
print(abs(-1.2))

#all(x): 반복 가능한 자료형(리스트 , 튜플, 문자열 , 딕셔너리, 집합등 for로 값을 출력할 수 있는 자료형)
#인수로 받아 x  가 모두 참이면 True 아니면 False
print(all([1,2,3]))
print(all([1,2,5,0]))

#any(x): x중 하나라도 참이 있으면 True, 모두 거짓이면 False
print(any([1, 2,3,0]))
print(any([None, 0, ""]))

#chr(i): 아스키 코드를 입력받아 그 코드에 해당하는 문자를 출력하는 함수.
print(chr(97))
print(chr(48))

#dir : 객체가 자체적으로 가지고 있는 변수나 함수를 보여줌.
print(dir([1,2,3]))
print(dir({"1":"a"}))

#divmod(a,b): a를 b 로 나눈 몫과 나머지를 튜플 형태로 돌려줌
print(divmod(7,3))

#enumerate:순서가 있는 자료형을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체로 돌려준다.(for 문과 자주 같이 사용됨.)
for i, name in enumerate(["body", "foo", "bar"]):
    print(i, name)
#자료형 현재 순서 알 수 있음.

#eval: 실행 가능한 문자열을입력받아 문자열을 실행한 결과값을 돌려주는 함수 
print(eval("1 + 2"))
print(eval("'hi'+'a'"))
print(eval("divmod(4,3)"))
