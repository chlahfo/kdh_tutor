import re

#메모장 텍스트 불러오기
f = open("parsing_data.txt", "r", encoding = 'UTF-8')
txt_cnt = f.read()
f.close()

#메모장 컴파일
compiler = re.compile(r"https://[\w\d]+[.]*.*?(?=\"|\s)", re.M)
link_list = compiler.findall(txt_cnt)

#컴파일 한 내용 메모장에 쓰기
a=""
for i in range(len(link_list)):
    a += str(link_list[i]) + "\n"
f = open("link_data_write.txt","w", encoding="UTF-8")
f.write(a)
f.close()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              