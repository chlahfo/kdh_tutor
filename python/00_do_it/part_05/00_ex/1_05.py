#생성자(Calculator) - 객체에 초깃값 설정할 필요 : __init__를 사용.
#객체 생성 시 자동 호출됨.

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

#객체 생성
a = FourCal(4, 2)

print(a.add())
print(a.div())




