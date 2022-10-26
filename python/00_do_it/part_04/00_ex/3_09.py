#with 문과 함께 사용하기
#파일 열고 닫는것을 자동으로 처리
with open("D:/miniFiles/kdh_tutor/python/00_do_it/part_04/00_ex/새파일3_09.txt", "w") as f:
    f.write("Life is too short, you need python")

#sys 모듈로 매개변수 주기
"""
import sys
args =sys.argv[1:]#argv 명령창에서 입력한 인수
for i in args:
    print(i)
"""
#입력 받은 인수를 for 문을 사용해 차례대로 하나씩 출력하는 예. 

#예시
import sys
args = sys.argv[1:]
for i in args:
    print(i.upper(), end="")