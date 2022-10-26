#주어진 자연수가 홀수인지 짝수인지 판별해주는 함수 (is_odd)를 작성해보자
def is_odd(number):
    if number % 2 == 1 :
        return True
    else:
        return False

aaa= is_odd(26)
print(aaa)