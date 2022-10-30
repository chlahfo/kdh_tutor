import sys
n = sys.stdin.readline().rstrip()#입력수 = 한계수

def han(n):
    a = 0
    # 1 ~ n 까지 동작(사이클에 해당하는 수 k)
    for k in range(1, int(n)+1):
        t_list = []
        if k > 99:
            ks = str(k)
            #ks 의 각 자릿수 동일한지 비교
            for i in range(len(ks)-2):
                if (int(ks[i+2]) - int(ks[i+1])) == (int(ks[i+1]) - int(ks[i])):
                    t_list.append(1)
                else:
                    t_list.append(0)
            #다 동일하면 a 카운트
            if all(t_list):
                a += 1
        else:
            a += 1
        
    return a

print(han(n))
    