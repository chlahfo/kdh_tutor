#for 문과 range 함수
a = range(10)
#0~10 숫자를 포함하는 range 객체를 만들어줌

#예시1
add = 0
for i  in range (1, 11):
    add+=i
    print(add)

#예시2
marks = [90, 25, 67, 45, 80]
for num in range(len(marks)):
    if marks[num] <60:continue
    print("%d번 학생 축하합니다. 합격입니다." %(num + 1))#0부터 인덱스 번호로 들어가서 1을 더해준거임