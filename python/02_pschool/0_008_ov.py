#각도기
def solution(angle):
    answer = 0
    if angle > 0 and angle < 90:
        answer = 1
    elif angle == 90:
        answer = 2
    elif angle > 90 and angle < 180:
        answer = 3
    else:
        answer = 4
    return answer
    
#리뷰요청
def solution(angle):
    return 2 if angle==90 else 1 if angle<90 else 4 if angle==180 else 3

#보관
def solution(angle):
    answer = (angle // 90) * 2 + (angle % 90 > 0) * 1
    return answer