#클래스의 상속-->  class 클래스 이름(상속할 클래스 이름) --> 라이브러리나 수정 허용 x 일때 사용됨.
#대부분 클래스 기능 확장에 주로 사용됨.
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second #a 의 b 제곱
        return result 

a= MoreFourCal(4, 2)
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())
print(a.pow())

#메서드 오버라이딩
"""
a = FourCal(4, 0)
a.div()#4나누기 0 --> 에러남
"""
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

a = FourCal(4, 0)
a.div()
