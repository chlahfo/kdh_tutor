#findall- 맞는 것 끼리 매치해서 리스트로 돌려준다.
import re
p = re.compile("[a-z]+")

result = p.findall("Life is too short")
print(result)