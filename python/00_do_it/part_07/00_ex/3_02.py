#전방 탐색
import re
p = re.compile(".+:")
m=p.search("http://google.com")
print(m.group())

#긍정형 전방 탐색(?=)
p = re.compile(".+(?=:)")
m=p.search("http://google.com")
print(m.group())

#부정형 전방 탐색(bat|exe 확장자 제외)(?!)
p = re.compile(".*[.](?!bat$|exe$).*$")
m=p.search("bee.bat bar.bat")
print(m)