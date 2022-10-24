#집합 자료형 파이썬 2,3 부터 지원
s1=set([1,2,3])
print(s1)
s2=set("Hello")
print(s2)
#중복 안됨, 순서 없음
#순서가 없어 인덱싱 불가하므로 사용하고 싶을 때는 list() 사용해서 리스트로 변환한 뒤, 사용

l1=list(s1)
print(l1)
print(l1[0])
t1=tuple(s1)
print(t1)
print(t1[0])