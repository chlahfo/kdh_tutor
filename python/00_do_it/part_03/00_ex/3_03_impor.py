#for 와 range 를 사용한 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end=" ")#해당 같은 단 일 때 줄내림을 하지 않기 위해 end 매개변수를 사용한 것이다.(end 매개변수라고 따로 있음)
    print("")#줄내림을 하기 위한 것이다.


#문자열 헷갈렸음
for i in range(2, 10):
    for j in range(1, 10):
        print("{} x {} = {}".format(i, j, i*j))
    print("{0:->10}{1:-<10}".format(i,"단"))


#print 함수에서 sep 과 end
#print 함수는 각 파라미터는 공백, 끝에는 개행문자가 기본인데, 이것을 각각 sep과 end 로 바꿔줄 수 있다.
print(1,2,3, sep=", ", end=" / ")
print(4,5,6, sep=", ", end=" / ")