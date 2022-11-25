#머쓱이보다 큰 사람
def solution(array, height):
    answer = 0

    for i in array:
        if i > height:
            answer += 1

    return answer

#보관
def solution(array, height):
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)