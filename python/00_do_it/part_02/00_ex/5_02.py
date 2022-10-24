#딕셔너리 관련 함수 
#Key 리스트 만들기
a={"name":"pey", "phone":"0119993323", "birth":"1118"}
aa=a.keys()
print(aa)#dict_keys 객체를 돌려줌.
#파이썬 2.7까지는 리스트를 돌려줌. 대신 메모리 낭비 발생.
#파이썬 3.0 은 dict_keys 객체를 돌려줌. 반환값으로 형식이 필요한 경우 list() 함수를 ㅎ사용한다.
aaa=list(aa)
print(aaa)
#다만 리스트로 변환 안해도 반복구문에서 사용 가능
#append, insert, pop, remove, sort 등은 사용 불가.

#Value 리스트 만들기
b=a
bb=b.values()#dict_values 객체 반환
print(bb)

#Key, Value 쌍 얻기
cc=a.items()
print(cc)#dict_item 반환

#clear 함수 사용

#b.clear()
a.clear()
print(b)
print(a)#놀랍게도 clear 함수가 a 에도 적용이 됨.. 둘 중 어느것에 써도..

a={"name":"pey", "phone":"0119993323", "birth":"1118"}
print(a.get("name"))
print(a.get("phone"))

#list.get(key) 와 list[key]는 동일한 결과를 주지만 없는 키의 값을 요청할 때는 get은 None을 반환하고, 후자는 에러메세지.

#딕셔너리 안에 찾으려는 Key 값이 없을 경우 미리 정해 둔 디폴트 값을 대신 가져오게 하고 싶을 때 get(x, "디폴트 값")을 사용하면 편리하다.
print(a.get("foo", "bar"))


#해당 Key 가 딕셔너리 안에 있는지 조사(in)
aaa = "name" in a
bbb = "email" in a
print(aaa, bbb)



