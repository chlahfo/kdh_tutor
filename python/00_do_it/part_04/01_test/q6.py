#사용자의 입력을 파일 (test.txt)에 저장하는 프로그램을 작성해보자.(단, 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야한다.)
user_input = input("저장할 내용을 입력하세요:")
f = open("D:/miniFiles/kdh_tutor/python/00_do_it/part_04/01_test/q6.txt", "a")
f.write(user_input)
f.write("\n")#입력한 내용을 줄 단위로구 구분하기 위해 줄바꿈 문자 삽입
f.close