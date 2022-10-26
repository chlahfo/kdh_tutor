#test.txt 파일에 "Life is too short"문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램이다. 해당 문자열을 출력하도록 수정해보자.
f1 = open("D:/miniFiles/kdh_tutor/python/00_do_it/part_04/01_test/q5.txt","w")
f1.write("Life is short")
f1.close()#여기서 닫아줘야 아래에서 읽고 출력이 가능.

f2 = open("D:/miniFiles/kdh_tutor/python/00_do_it/part_04/01_test/q5.txt","r")
print(f2.read())
f2.close()