#객체 변수 calue 100 이상의 값은 가질 수 없도록 제한하는 Max~ 클래스 ㄹ를 만들어보자 . 즉, (책 참고)
class Calculator:
    def __init__(self):
        self.value = 0
    def add(self, val):
        self.value += val

class MaxLinitCalculator(Calculator):
    def add(self, val):
        self.value += val

        if self.value >= 100:
            self.value = 100            

cal = MaxLinitCalculator()
cal.add(50)
cal.add(60)
print(cal.value)