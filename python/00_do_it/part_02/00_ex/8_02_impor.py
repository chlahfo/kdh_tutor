#b 변수를 생성 할 때 a 변수 값을 가져오면서 a dhk ekfms tnthfmf rkfmzlehfhr qksemsms qkdqjq

#[:] 사용
a=[1,2,3]
b=a[:]#리스트 전체 슬라이싱
print(id(a), id(b))
a[1]=4
print(a, b)

#copy 모듈 사용
from copy import copy
a = [1,2,3]
b=copy(a)
b[1]=a
print(a, b)