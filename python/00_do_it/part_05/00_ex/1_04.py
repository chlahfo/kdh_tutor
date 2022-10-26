#사칙연산 클래스 만들기
class FourCal:
    def setdata(self, first, second):#self에는 객체 a 가 자동으로 전달됨. self를 js 의 this 라고 생각하면 편함. 관례적으로 self 라고 이름을 지정함.
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
a = FourCal()
b = FourCal()

#데이타 셋팅
a.setdata(4, 2)
b.setdata(3, 7)

#결과 확인
print(a.add())
print(b.add())


#잘 사용하진 않지만 클래스를 통해 메서드 호출도 가능함.