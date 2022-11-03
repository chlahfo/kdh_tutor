# sub 구문 사용 시 참조 구문 사용
import re
p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
print(p.sub("\g<phone> \g<name>","park 010-1234-1234"))# ==g<2> g<1>

#sub 메서드에 매개변수로 함수 넣기
def hexreple(match):
    "Return the hex string for a decimal number"
    value = int(match.group())
    return hex(value)
p = re.compile(r"\d+") 
m = p.sub(hexreple, "Call 65490 for printing, 49152 for user code.")
print(m)

