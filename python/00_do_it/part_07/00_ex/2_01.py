import re
p = re.compile("[a-z]+")

# match
# 맨 처음부터 맞는 영역까지 잡는다. 단, 무조건 맨 처음부터 잡으므로 맨 처음이 맞지 않는다면 return 을 반환한다.
m = p.match("python is language.")
m1 = p.match("python is language.")
print(m, m1)

#match 의 결과로 보통 match 객체 또는 None 을 돌려주기 때무네 파이썬 정규식 프로그램은 보통 다음과 같은 흐름으로 작성한다.
p = re.compile("[a-z]+")
m = p.match("apple is very delicious")
if m:
    print("Match found:", m.group())
else:
    print("No match")