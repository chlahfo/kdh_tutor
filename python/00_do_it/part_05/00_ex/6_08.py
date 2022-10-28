#random - > 난수 발생
import random
print(random.random())#0.0과 1.0 사이의 난수
print(random.randint(1, 10))# 1과 10 사이의 정수


#활용 예
def random_pop(data):
    number = random.randint(0, len(data)-1)
    return data.pop(number)

if __name__ == "__main__":
    data = [1,2,3,4,5]
    while data:print(random_pop(data))

def random_pop2(data):
    num = random.choice(data)#리스트에서 무작위로 하나를 선택하여 돌려줌.
    data.remove(num)
    return num

data=[1,2,3,4,5]
random.shuffle(data)# 무작위 섞기
print(data)

#webbrowser:기본 웹브라우저 자동 실행
import webbrowser
webbrowser.open("www.google.com")
webbrowser.open_new("www.naver.com")