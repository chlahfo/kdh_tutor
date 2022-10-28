#filter 와 lambda 를 사용하여 리스트 [1, -2, 3, -5, 8, -3]에서 음수를 모두 제거하자.
aaa= list(filter(lambda x: x > 0, [1, -2, 3, -5, 8, -3]))
print(aaa)