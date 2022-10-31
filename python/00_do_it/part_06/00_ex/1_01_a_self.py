#구구단 프로그램
#혼자 도전해보기
def mul99(x):
    for i in range(1, 10):
        print("{} x {} = {}".format(x, i, x*i))

for j in range(2, 10):
    print("{:-<10}{}{:->10}".format("",j,""))
    mul99(j)
    print("{:-^20}".format("----"))