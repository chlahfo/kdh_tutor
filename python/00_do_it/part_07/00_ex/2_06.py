#모듈 단위로 수행하기
import re
"""
p=re.compile("[a-z]+")
m=p.match("python")
"""
m=re.match("[a-z]+","python Dont")
print(m.group())
