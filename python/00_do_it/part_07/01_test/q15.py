result=[]
num_list = input().split()

for nums in num_list:
    #d_list 0 초기화
    d_list=[]
    for i in range(0, 10):
        d_list.append(0)
    #d_list 숫자 넣기
    for i in range(len(nums)):
        num = int(nums[i])
        d_list[num] += 1
    if d_list.count(1) == 10:
        result.append("true")
    else:
        result.append("false")

print(" ".join(result))