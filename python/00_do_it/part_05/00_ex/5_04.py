#open ->  파일 이름 + 읽ㄱ기 방법(기본 w,r,a,b(wra 와 함께 사용))
f = open("D:/miniFiles/kdh_tutor/python/00_do_it/part_05/00_ex/test_file.txt", "w")
f.write("this is open test")
f.close()

f = open("D:/miniFiles/kdh_tutor/python/00_do_it/part_05/00_ex/test_file.txt", "rb")
a = f.read()
print(a)
f.close()

