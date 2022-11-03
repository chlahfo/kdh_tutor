# 리스트 더하기와 extend 함수
a = [1,2,3]
print(id(a))
a = a + [4, 5]
print(a, id(a))

a = [1,2,3]
print(id(a))
a.extend([4, 5])
print(a, id(a))
#차이점은 전자는 재할당되므로 a 의 id 값이 변하는 반면 extend 를 하면 id 값이 변하지 않는다. 따라서 a = b 를 했을때, b 의 값은 전자는 b가 a 의 값을 따라가지 않는 반면 후자는 b 는 a 의 값을 따라가게 된다는 차이점이 있다