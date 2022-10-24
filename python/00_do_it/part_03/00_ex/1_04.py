#elif 쓰기
#주머니에 돈이 있으면 택시, 돈은 없지만 카드가 있으면 택시, 돈도 없고 카드도 없으면 걷기

#if 와 else 만 쓸때
pocket=["paper", "cellphone"]
card = True
if "money" in pocket:
    print("택시")
else:
    if card:
        print("택시")
    else:
        print("걷기")

#elif 쓰기 (++여러개도 쓰기 가능함)
pocket=["paper", "cellphone"]
card = True
if "money" in pocket:
    print("택시")
elif card:
    print("택시")
else:
    print("걷기")
