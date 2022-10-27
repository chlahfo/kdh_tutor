#클래스 변수

#클래스 생성
class Family:
    lastname = "김"

print(Family.lastname)

#객체 생성- > Family 클래스의 인스턴스 생성.
a = Family()
b = Family()

print(a.lastname)
print(b.lastname)

Family.lastname = "박"
print(Family.lastname)
print(a.lastname)
print(b.lastname)

#클래스 변수는 해당 클래스의 인스턴스의 변수 값이랑 공유됨.
id(Family.lastname)
id(a.lastname)
id(b.lastname)

#사실 클래스 변수보다 객체변수를 더 많이 사용.