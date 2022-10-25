#readlines 함수 사용
f = open("D:/miniFiles/kdh_tutor/python/00_do_it/part_04/00_ex/새파일3_02.txt", "r")
lines = f.readlines()#각각의 줄을 요소로 갖는 리스트로 돌려준다.
for line in lines:
    print(line)
f.close()