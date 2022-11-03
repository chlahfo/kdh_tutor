#Greedy vs Non-Greedy
import re
s="<html><head><title>Title</title>"
len(s)
print(re.match("<.*>", s).span())
print(re.match("<.*>", s).group())

print(re.match("<.*?>", s).group())#최소한의 반복
#*?, +?, ??, {m,n}?
