#for문
#전형적인 for 문
test_list=["one", "two", "three"]
for i in test_list:
    print(i)

#다양한 for 문의 사용(튜플 값 대입과 비슷하다고 생각하면 됨.)
a=[(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)

#for 문 응용
#총 5명의 학생이 시험을 보앗는데 시험 점수가 60점이 넘으면 합격이고 그렇지 않으면 불합격이다. 합격인지 불합격인지 결과를 보여주시오.
marks=[90, 25, 67, 45, 80]
num = 0
for mark in marks:
    num += 1

    if mark>=60:
        print("%d번 학생은 합격입니다." % num)
    else:
        print("%d번 학생은 불합격입니다." % num)

#for  문과 continue 문
marks=[90, 25, 67, 45, 80]
num = 0
for mark in marks:
    num += 1
    if mark < 60: continue
    print("%d번 학생 축하합니다. 합격입니다." %num)
