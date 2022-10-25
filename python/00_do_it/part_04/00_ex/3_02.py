#파일을 쓰기 모드로 열어 출력값 적기
f = open("python/00_do_it/part_04/00_ex/새파일3_02.txt", "w")
for i in range(1, 11):
    data = "%d번째 줄입니다 \n" %i
    f.write(data)
f.close()#파일에 결과값 출력 

for i in range(1, 11):
    data1 = "%번쨰 줄입니다.\n" %i
print(data1)#모니터 출력
