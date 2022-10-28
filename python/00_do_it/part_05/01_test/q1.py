#Calculator를 상속하는 UpgradeCalculator 를 만들고, 값을 뺄수 있는 minus 메서드를 추가해보자.
class Calculator:
    def __init__(self):
        self.value=0
    def add(self, val):
        self.value += val
        return self.value

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val
        return self.value

cal=UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value)