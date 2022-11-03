#문자열 바꾸기
#sub 메서드
import re 
p = re.compile("(blue|white|red)")
m = p.sub("colous","socks and red shoes",count=1)#문자열 형태 반환
print(m)
#subn 메서드
m = p.subn("colous","socks and red shoes",count=1)#튜플 형태 반환
print(m)

