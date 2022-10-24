#문자열 관련 함수

#문자 갯수 세기 (count)
a="hobby"
b_num=a.count("b")
print(b_num)

#위치 알려주기1 (find)
a="Python is the best choice"
bb=a.find("b")
print(bb)#b가 처음 나온 위치 반환
kk=a.find("k")
print(kk)#문자나 문자열이 존재하지 않으면 -1 반환
aa=a.find("is")
print(aa)#단어의 첫 위치 반환

#위치 알려주기2(index)
a="Life is too short"
print(a.index("t"))#위치는 반환하지만 만약 문자열이 존재하지 않으면 오류가 발생함.


#문자열 삽입
aaa=",".join("abcd")#각 문자 사이에 ,를 삽입함. 리스트나 튜플도 입력으로 사용 가능
print(aaa)

bbb=",".join(["a", "b", "c", "d"])
print(bbb)

#소문자 -> 대문자

a="hi"
bb=a.upper()#기존 a 문자열은 바뀌지 않음.
print(bb)
b="HI"
bb=b.lower()
print(bb)

#왼쪽 공백 지우기
a="   뭔가 좀 그런 느낌이 듦    "
b="123"
aa=a.lstrip()
print(aa)
print(b+aa+b)

#오른쪽 공백 지우기
a2=a.rstrip()
print(a2)
print(b+a2+b)

#양쪽 공백 지우기
a3=a.strip()
print(b+a3+b)

#문자열 나누기
a="Lift is too short"
aa=a.split()
print(aa)
b="a:b:c:d"
bb=b.split(":")
print(bb)


