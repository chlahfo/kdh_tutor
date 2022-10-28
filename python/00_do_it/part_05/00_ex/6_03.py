#pickle ==> 어떤 자료형이든 저장하고 불러올 수 있다.!!!
import pickle
f = open("D:/miniFiles/kdh_tutor/python/00_do_it/part_05/00_ex/test_file_6_02.txt", "rb")
data = pickle.load(f)
print(data)