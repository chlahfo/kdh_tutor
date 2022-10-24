#while 문 기본 구조 
treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    print("나무를 %d 번 찍었습니다." %treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")


#while 문 만들기
prompt="""
1. Add
2. Del
3. List
4. Quit

Enter number:
"""
num = 0
while num !=4:
    print(prompt)
    num = int (input())

#break
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee -= 1
    print("남은 커피의 양은 %d개입니다." %coffee)
    if coffee == 0:
        print("커피가 다 떨어져 판매를 중지합니다.")
        break