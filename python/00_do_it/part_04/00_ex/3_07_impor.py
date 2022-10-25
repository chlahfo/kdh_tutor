#read 함수 사용
f = open("D:/miniFiles/kdh_tutor/python/00_do_it/part_04/00_ex/새파일3_02.txt", "r")
data = f.read()#전체를 문자열로 돌려준다.
print(data)
f.close()