#컴파일 옵션
#DOTALL, S
import re
p=re.compile("a.b", re.DOTALL|re.IGNORECASE)
m=p.match("a\nb")
print(m.group())

#IGNORECASE, I |re.IGNORECASE

