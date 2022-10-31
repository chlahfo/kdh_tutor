#match 객체의 메서드
#group
import re
p = re.compile("[a-z]+")
m = p.match("bob is BOB bob is BOB bob is BOB bob is BOB")
print(m.group())
print(m.start())
print(m.end())
print(m.span())

s = p.search("22 bob is BOB bob is BOB bob is BOB bob is BOB")
print(s.group())
print(s.start())
print(s.end())
print(s.span())