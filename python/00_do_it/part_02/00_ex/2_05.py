#문자열 인덱싱과 슬라이싱
a="Life is too short, you need Python"

print(len(a))#길이

print(a[3], a[-1])#인덱싱
print(a)#인덱싱 된다고 원래 꺼가 잘리진 않음

b=a[0]+a[1]+a[2]+a[3]
print(b)
bb=a[0:4]#[시작번호:끝번호] - 끝번호는 미포함
print(bb)

c=a[0:5]
print(c)#공백도 포함

print(a[0:2], a[5:7], a[12:17])

d=a[19:]
print(d)#끝 번호 부분을 생략하면 시작 번호부터 그 문자열의 끝까지 

e=a[:17]
print(e)#시작 번호 부분을 생략하면 처음부터 끝 번호 전까지 뽑아냄

f=a[:]
print(f)#시작번호 끝번호를 둘 다 생략하면 처음부터 끝까지 뽑아냄

g=a[19:-7]
print(g)#또한 -7 기호도 사용 가능

#슬라이싱으로 문자열 나누기
a="20010331Rainy"
date=a[:8]
weather=a[8:]
print(date)
print(weather)

year=a[:4]
day=a[4:8]
weather[8:]
print(year, day, weather)