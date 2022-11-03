class Calculator:
    def __init__(self, lists):
        self.lists = lists
    def setdata(self, lists):
        self.lists = lists
    def sums(self):
        result = sum(self.lists)
        return result
    def avg(self):
        if len(self.lists) != 0:
            result = sum(self.lists)/len(self.lists)
        else:
            result = 0
        return result

cal1 = Calculator([1,2,3,4,5])
print(cal1.sums())
print(cal1.avg())
cal2 = Calculator([6,7,8,9,10])
print(cal2.sums())
print(cal2.avg())