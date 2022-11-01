#그룹핑
import re
p = re.compile("(ABC)+")
m = p.search("ABCABCABC OK?")
print(m)
print(m.group(0))

p = re.compile(r"\w+\s+\d+[-]\d+[-]\d+")
m = p.search("park 010-1234-1234")
print(m)
print(m.group())

p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m)
print(m.group(1))
print(m.group(2))
print(m.group(3))

#그룹핑 문자열 재참조
p = re.compile(r"(\b\w+)\s+\1")
m = p.search("Paris in the the spring").group()
print(m)

#그룹핑된 문자열에 이름붙이기
p=re.compile(r"(?P<aaa>\w+)\s+((\d+)[-]\d+[-]\d+)")
m=p.search("park 010-1234-1234")
if m:
    print(m.group("aaa"))
else:
    print("No match")

p = re.compile(r"(?P<word>\b\w+)\s+(?P=word)")
m = p.search("Paris in the the the spring").group()
print(m)#재참조