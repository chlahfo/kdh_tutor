#홍길동씨의 과목별 점수는 다음과 같다. 홍길동 씨의 평균 점수를 구해보자.
#과목 국어 80, 영어 75, 수학 55
test_resulte={"korean":80, "eng": 75, "math": 55}
sjt_name=test_resulte.keys()
sjt_name=list(sjt_name)
sjt_num=len(test_resulte)
stack = 0

while sjt_name:
    name=sjt_name.pop()
    stack+=test_resulte.get(name)
    
total_score = stack / sjt_num
print("평균 점수는 {:0.1f}입니다" .format(total_score))
