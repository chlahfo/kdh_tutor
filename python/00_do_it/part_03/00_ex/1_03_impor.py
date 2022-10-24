#x in s, x not in s
a = 1 in [1,2,3]
b = 1 not in [1,2,3]
print(a, b)

a = "a" in ("a","b","c")
b = "j" not in ("a","b","c")
print(a, b)

#만약 주머니에 돈이 있으면 택시를 타고, 없으면 걸어 가라.
pocket = ["paper", "cellphone", "money"]
if "money" in pocket:
    print("택시")
else:
    print("걷기")

#아무일도 하지 않는 조건문
#주머니에 돈이 있으면 가만히 있고 주머니에 돈이 없으면 카드를 꺼내라
pocket=["paper", "money", "cellphone"]
if "money" in pocket:
    pass
else:
    print("카드 꺼내기")