#피자 나눠 먹기(1)
def solution(n):
    answer = n // 7 + (n % 7 != 0)
    return answer

#리뷰요청-이게 왜 됨..?
def solution(n):
    return (n - 1) // 7 + 1