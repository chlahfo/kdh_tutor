#이 파일의 내용 중 "java"라는 문자열을 "python"으로 바꾸어 저장해보자.
f = open("D:/miniFiles/kdh_tutor/python/00_do_it/part_04/01_test/q7.txt", "w")
f.write("Life is to short \nyou need java")
f.close()

f = open("D:/miniFiles/kdh_tutor/python/00_do_it/part_04/01_test/q7.txt", "r")
body = f.read()
f.close()

body = body.replace("java", "python")

f = open("D:/miniFiles/kdh_tutor/python/00_do_it/part_04/01_test/q7.txt", "w")
f.write(body)
f.close