#자료형의 참과 거짓
#비어있는 것은 거짓, 아닌것은 참. 숫자는 0 거짓 이외는 참

a=[1,2,3,4]
while a:#a 가 참일동안
    print(a.pop())#리스트의 요소를 꺼내고 삭제

if[]:
    print("참")
else:
    print("거짓")

if [1,2,3]:
    print("참")
else:
    print("거짓")

#bool 자료형의 참과 거짓 식별
print(bool("python"))
print(bool(""))
print(bool([1,2,3]))
print(bool([]))
print(bool(0))
print(bool(3))
    