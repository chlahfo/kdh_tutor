#[1,3,5,4,2] 리스트를 [5,4,3,2,1]로 만들어보자.
a=[1,3,5,4,2]
a.sort(reverse=True)
print(a)

#or
a=[1,3,5,4,2]
a.sort()
a.reverse()
print(a)