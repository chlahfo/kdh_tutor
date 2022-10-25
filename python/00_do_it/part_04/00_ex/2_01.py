#사용자 입력
#input 사용 => 입력되는 모든 것을 문자열로 취급
#프롬프트 값을 띄워서 사용자 입력받기
a = input("아무 문자열이나 입력하세요:")
print(a)

#print 자세히 알기- 사용 예시
a = 123
print(a)
a = "Python"
print(a)
a = [1,2,3]
print(a)

#큰따옴표(")로 둘러쌓인 문자열은 + 연산과 동일하다.
print("life" "is" "too short")
print("life"+"ls"+"too short")

#문자 띄어쓰기는 콤마로 한다.
print("Life", "is", "too short")

#한 줄에 결과값 출력하기
for i in range(10):
    print(i, end =" ")
