#len- 입력값 s 의 길이 (요소 전체 개수)를 돌려주는 함수
print(len("python"))
print(len([1,2,3]))
print(len((1, "a")))

#list-반복 가능한 자료형 s 를 입력받아 리스트로 돌려주는 함수 
print(list("python"))
print(list((1,2,3)))

#단, list함수에 리스트를 입력으로 주면 똑같은 리스트를 복사하여 돌려준다. 단 그렇게 하였을 경우, id 값은 다르다.
a= [1,2,3]
b = list(a)
print(b)
print(id(a), id(b))

#map - 1. f 함수 2. 반복 가능한 자료형 --> 입력 받은 자료형의 각 요소를 f 함수가 수행한 결과를 묶어서 돌려주는 함수이다.
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1,2,3,4])
print(result)

def two_times(x):return x *2
result= list(map(two_times, [1,2,3,4]))
print(result)

result = list(map(lambda a: a*2, [1,2,3,4]))
print(result)

#max 1. 반복 가능한 자료형 -> 최댓값 돌려줌
print(max([1,2,3]))
print(max("python"))

#min 1. 같음. -> 최솟값 돌려줌
print(min([1,2,3]))
print(min("python"))

#oct -> 정수 형태의 숫자를 8진수 문자열로 바꾸어 돌려주는 함수.
print(oct(34))
print(oct(12345))





