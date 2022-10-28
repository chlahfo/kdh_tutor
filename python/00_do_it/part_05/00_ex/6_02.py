#pickle-->객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈
import pickle
f = open("D:/miniFiles/kdh_tutor/python/00_do_it/part_05/00_ex/test_file_6_02.txt", "wb")
data = {1:"python", 2:"you need"}
pickle.dump(data, f)
f.close()

