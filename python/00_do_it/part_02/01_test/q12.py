#파이썬은 다음처럼 동일한 값에 여러 개의 변수를 선언할 수 있다. 다음과 같이 a,b 변수를 선언한 후 a 의 첫번쨰 요솟값을 변경하면 b의 값은 어떻게 될까? 그리고 이런 결과가 나오는 이유에 대해 설명해보자.
a=b=[1,2,3]
a[1]=4
print(b)
#b=[1,4,3]이 됨. 리스트의 메모리 주소를 참조하는 변수는 a 와 b 둘 다 이기 때문에 리스트의 요소 값을 변경하면 b 의 값또한 변경된다.
