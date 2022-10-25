#모든 줄을 읽어서 화면에 출력
#f나 line 도 바꿔도 됨
files = open("D:/miniFiles/kdh_tutor/python/00_do_it/part_04/00_ex/새파일3_02.txt","r")
while True:
    lines = files.readline()
    if not lines:break  #readline()은 더 이상 읽은 줄이 없으면 None을 출력하므로 -> break 가 실행된다.
    print(lines)
files.close()