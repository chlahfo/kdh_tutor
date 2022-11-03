import re
#문자열 바꾸기 a:b:c:d 
s="a:b:c:d"
p = re.compile("[^\w]")
m = p.sub("#", s)
print(m)

s=s.split(":")
s="#".join(s)
print(s)