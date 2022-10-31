#findall- 맞는 것 끼리 매치해서 리스트로 돌려준다.
import re
p = re.compile("[a-z]+")

result = p.finditer("Life is too short")
print(result)

for i in result:
    print(i)

#반복 가능한 match 객체들로 돌려줌