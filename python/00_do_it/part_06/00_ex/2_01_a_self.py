#10 미만의 자연수에서 3과 5의 배수를 구하면 3,5,6,9 이다. 이들의 총합은 23이다.
#1000 미만의 자연수에서 3의 배수와 5의 배수 총합을 구하라
def mul_sum(endnum, *arg):
    mulnum_list = []

    for k in arg:
        for i in range(1, endnum):
            if i % k == 0:
                mulnum_list.append(i)
    
    mulnum_list=set(mulnum_list)
    sums = sum (mulnum_list)
    return sums

print(mul_sum(1000,3,5))