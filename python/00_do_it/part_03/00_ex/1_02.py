#연산자 사용
x=3
y=2
print(x>y)
print(x<y)
print(x==y)
print(x!=y)

#3000원 이상 돈 있으면 택시 아니면 걸어서
money =2000
if money >= 3000:
    print("택시 타고 집")
else:
    print("걸어서 집")

#3000원 이상 있거나, 카드가 있으면 택시 아니면 집
money =2000
card = True
if money >= 3000 or card:
    print("택시")
else:
    print("집")

