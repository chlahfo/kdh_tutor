#피자 나눠 먹기(3)
def solution(slice, n):
    answer = n // slice + (n % slice != 0)
    return answer

#리뷰 요청 1
def solution(slice, n):
    return ((n - 1) // slice) + 1