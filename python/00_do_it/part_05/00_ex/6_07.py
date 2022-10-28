#calendar - 달력ㅂ기
import calendar
print(calendar.calendar(2015))
print(calendar.prcal(2015))
print(calendar.prmonth(2022, 10))

print(calendar.weekday(2022, 10, 28))#월~ 0~
print(calendar.monthrange(2015, 12))#입력받은 닿의 1일이 무슨 요일인지, 며칠까지 있는지.