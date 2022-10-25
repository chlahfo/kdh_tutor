#프로그램의 외부에 저장된 파일을 읽는 여러가지 방법
#readline 함수 사용
f = open("D:/miniFiles/kdh_tutor/python/00_do_it/part_04/00_ex/새파일3_02.txt","r")
line = f.readline()
print(line)
f.close()
#읽기 모드 -> 첫번째줄 읽어 출력