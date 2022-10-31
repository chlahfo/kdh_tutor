def menuAdd():
    f = open("mymemo401_a.txt", "w")
    f.close()

def menuAddCnt(s):
    f = open("mymemo401_a.txt", "a")
    f.write(s)
    f.close()

def menuRead():
    f = open("mymemo401_a.txt", "r")
    cnt = f.read()
    print(cnt)
    f.close()

n1 = input("메모장 기능을 숫자로 선택해주세요. \n 1. 메모장 만들기 또는 기존 내용 삭제 \n 2. 메모장 쓰기 \n 3. 메모장 내용 읽기 \n 입력 : ")
if n1 == "1" :
    menuAdd()
elif n1 == "2":
    t = input("메모장에 쓸 내용을 입력해주세요:\n")
    menuAddCnt(t)
elif n1 == "3":
    menuRead()
else:
    print("잘못 선택하였습니다. 다시 실행 후 입력해주세요.")




