#n, stacks, sum
import sys
n = int(sys.stdin.readline().rstrip())


for i in range(0, n):
    st = sys.stdin.readline().rstrip()
    sum = 0
    stacks = 0
    
    for j in range(0, len(st)):
        if st[j] =="O":
            if j >= 0 and st[j - 1] == "O":
                stacks += 1
            else:
                stacks = 1
            sum += stacks
        else :
            stacks = 0

    print(sum)



            
    
    