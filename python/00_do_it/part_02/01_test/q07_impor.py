#["Life","is", "too", "short"] 리스트를 List is too short 무자열로 만들어 줄력해보자.
#문자열 나누기는 split 합치기는 join
from unittest import result


a=["Life","is", "too", "short"]
result = " ".join(a)
print(result)

back_s = result.split()
print(back_s)
