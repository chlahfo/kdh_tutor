#shutil - 파일을 복사
import shutil
shutil.copy("D:/miniFiles/kdh_tutor/python/00_do_it/part_05/00_ex/test_file.txt", "D:/miniFiles/kdh_tutor/python/00_do_it/part_05/00_ex/text_file_copy.txt")

#glob - 특정 디렉터리 파일 이름 모두 리스트로 
import glob
print(glob.glob("D:/miniFiles/*"))

#tempfile - 파일을 임시로 만들어 사용. 
import tempfile
filename = tempfile.mktemp()
print(filename)

f = tempfile.TemporaryFile()
f.close()