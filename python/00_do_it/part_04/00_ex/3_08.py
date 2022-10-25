#파일에 새로운 내용 추가하기
f = open("D:/miniFiles/kdh_tutor/python/00_do_it/part_04/00_ex/새파일3_02.txt", "a")
for i in range(11, 20):
    data = "%d번쨰 줄입니다.\n" %i
    f.write(data)
f.close()