#풀이 봄
import re
pat = re.compile(".*[@].*[.](?=com$|net$).*$")

print(pat.match("pahkey@gmail.com"))
print(pat.match("kim@daum.net"))
print(pat.match("kim@daum.ko"))
print(pat.match("lee@myhome.co.kr"))