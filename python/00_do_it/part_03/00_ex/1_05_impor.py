#if 문 한 줄 쓰기- 그냥 아랫줄 올리기같음
pocket=["paper", "money", "cellphone"]
if "money" in pocket: pass
else: print("카드를 꺼내라")

#조건부 표현식
score = 60
if score >= 60:
    message = "success"
else:
    message = "failure"
print(message)

message = "success" if score >= 60 else "failure"
print(message)

#가독성에 유리하고 한줄 작성이 가능하여 활용성이 좋음.