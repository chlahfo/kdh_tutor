#search - 매치하는 곳부터 매치하지 않는 곳 까지.
import re
p = re.compile("[a-z]+")
m = p.search("The txt is very short")
print(m)

if m :
    print("검색된단어의 일부:", m.group())
else:
    print("검색된 단어 없음") 