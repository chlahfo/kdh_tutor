#리스트 내포 사용하기
#리스트 안에 for 문을 포함하는 리스트 내포를 사용하면 좀 더 편리하고 직관적인 프로그램을 만들 수 있다.
a=[1,2,3,4]
result=[]
for num in a:
    
    result.append(num*3)

print(result)

#짝수에만 3을 곱하여 감기
result = [num *3 for num in a if num % 2 == 0] #표현식 for 항목 if 조건
print(result)

a = [1,2,3,4]
result = [num*10 for num in a if num % 2 == 0]#if 부분 생략 가능함.
print(result)

#for 문 2개 이상 사용하여 리스트 내포하기
result = [x * y for x in range (2, 10) if x % 3 == 0 for y in range(1,10) if y % 4 == 0]
print(result)
