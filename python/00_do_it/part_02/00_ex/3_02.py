#리스트 연산 :문자열 똑같

#리스트 더하기
a=[1,2,3]
b=[4,5,6]
print(a+b)

print(a*3)

#리스트 길이 구하기
print(len(a))

#추가
print(str(a[2])+"hi")

#리스트 수정과 삭제
a=[1,2,3]
a[2]=4
print(a)
del a[1]
print(a)

a=[1,2,3,4,5,6]
del a[2:]
print(a)

