n = int(input("구구단을 출력할 숫자를 입력하세요(2~9)"))
list_n = []
for i in range(1, 10):
    list_n.append(n*i)
print(" ".join(map(str, list_n)))
