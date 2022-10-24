#연관배열 해시
#딕셔너리 자료형

#딕셔너리 쌍 추가, 삭제
a={1:"a"}
a[2]="b"
print(a)

a["name"] ="pey"
print(a)

a[3]=[1,2,4]
print(a)

#딕셔너리 요소 삭제 
del a[1]
print(a)

#Key 를 사용해 Value 얻기
grade = {"pey": 10, "julliet":99}
print(grade["pey"])
print(grade["julliet"])

a={1:"a", 2:"b"}
print(a[1], a[2])

a={"a":1, "b":2}
print(a["a"], a["b"])
#중복 키를 사용하지 말것
#key 에 리스트 사용 불가. 단 튜플은 가능.. 리스트는 변할 수 있으므로 사용이 불가한 것.

aaa="test"
test1={aaa:"12"}
print(test1[aaa])
print(test1["test"])
# 근데 또 변수는 사용 가능함.. 이게 뭐야,..