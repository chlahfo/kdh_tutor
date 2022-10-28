#ord -문자의 아스키 코드를 돌려줌(chr 함수와 반대)
print(ord("a"))
print(ord("0"))

#pow(x,y) => x 의 y 제곱의 결괏값 돌려줌
print(pow(2,4))
print(pow(3,3))

#range([start], stop, [step])입력받은 숫자에 해당하는 범위값을 반복 가능한 객체로 돌려줌.
#start 기본 0 step 기본 1

#인수가 1개 => stop 값 5 외에 나머지 기본값
print(list(range(5)))

#인수가 2개 => start 값 5, stop값 10
print(list(range(5,10)))

#인수가 3개 => step 은 각 요소 사이에 늘어나는 숫자
print(list(range(1,10,2)))
print(list(range(-1,-10,-2)))


#round : 숫자를 입력받아 반올립
print(round(4.6))
print(round(3.1))

#sorted: 리스트를 정렬해서 결과값으로 돌려줌. 이 때 원본 리스트는 변하지 않음(sort()는 원본 함수를 바꾸며 그것을 따로 반환해주지 않음)
a = [3,2,5]
print(a)
print(sorted(a))
print(a)
a.sort()
print(a)

#str : 문자열 형태로 객체를 변환하여 돌려주는 함수
print(str(3))
print(str("hi"))
print(str("hi".upper()))

#sum : 리스트나 튜플의 모든 요소의 합을 돌려줌.
print(sum([1,2,3]))
print(sum((4,5,6)))

#tuple: 반복 가능한 자료형을 입력받아 튜플 형태로 바꾸어 돌려주는 함수이다.
print(tuple("abc"))
print(tuple([1,2,3]))
print(tuple((1,2,3)))

#type: 입력값의 자료형이 무엇인지 알려주는 함수
print(type("abc"))
print(type([]))
print(type(open("test.txt", "w")))

#zip: 동일한 갯수로 이루어진 자료형을 묶어주는 역할을 하는 함수(iterable반복 가능한 자료형을 여러개 입력할 수 있는 의미)-- > 같은 인덱스 끼리 묶어줌
print(list(zip([1,2,3], [4,5,6])))
print(list(zip([1,2,3], [4,5,6], [7,8,9])))
print(list(zip("abc","def")))
