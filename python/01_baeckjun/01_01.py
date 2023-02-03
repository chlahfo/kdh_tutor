#Hello world
print("Hello World!")

while True:
    point = int(input("포인트 입력:"))
    if point == 0:
        break
    num = point //10
    for i in range(num):
        print("*", end="")
    print()