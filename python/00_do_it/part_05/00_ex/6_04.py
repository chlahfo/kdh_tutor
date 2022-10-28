#os
#os.environ -내 시스템의 환경 변수 값
import os
print(os.environ)
print("\n{0:ㅡ^125}\n".format(""))
print(os.environ["PATH"])

#os.chdir - 현재 디렉터리 위치 변경 가능
print(os.getcwd())
os.chdir("C:/WINDOWS")

#os.getcwd - 현재 자신의 디렉터리 위치 받기
print(os.getcwd())

#os.system("dir")- 시스템 명령어 호출
os.system("dir")

#os.popen
f = os.popen("dir")
print(f.read())



#기타 유용한 os 관련 함수// os.mkdir, os.rmdir, os.unlink, os.rename
os.mkdir("D:/miniFiles/kdh_tutor/python/00_do_it/part_05/00_ex/test_dir")
os.mkdir("D:/miniFiles/kdh_tutor/python/00_do_it/part_05/00_ex/test_dir2")
os.rmdir("D:/miniFiles/kdh_tutor/python/00_do_it/part_05/00_ex/test_dir")
