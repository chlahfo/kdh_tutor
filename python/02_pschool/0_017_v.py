#짝수 홀수 개수
def solution(num_list):
    even_num = len(list(filter(lambda x: x % 2 == 0, num_list)))
    odd_num = len(num_list) - even_num
    answer = [even_num, odd_num]
    return answer

#보관1
def solution(num_list):
    answer = [0,0]
    for n in num_list:
        answer[n%2]+=1
    return answer

#보관2
def solution(num_list):
    div_num_list = list(map(lambda v: v % 2, num_list))
    return [div_num_list.count(0), div_num_list.count(1)]