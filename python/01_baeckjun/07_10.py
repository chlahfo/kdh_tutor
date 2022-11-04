import sys
n=int(sys.stdin.readline().rstrip())
tf=[]

#단어 사이클링
for i in range(n):
    #알파벳 자리 만들어놓기
    alpa=[]
    for j in range(97, 123):
        alpa.append(0)

    #단어 쓰기
    s=sys.stdin.readline().rstrip()
    for k in range(len(s)):
        #둘째자리부터 검사
        if k > 0:
            #전꺼와 같을때
            if s[k] == s[k-1]:
                alpa[ord(s[k])-97] += 1
            #전꺼와 다를 때
            else:
                #전에 나온적 없는 알파벳이면
                if alpa[ord(s[k])-97] == 0:
                    alpa[ord(s[k])-97] += 1
                #전에 나온적 있는 알파벳이면
                else:
                    tf.append(0)
                    break
        else: 
            alpa[ord(s[k])-97] = 1
        
    #끝까지 겹치는게 없을 때.
    if i == len(tf) :
        tf.append(1)
print(sum(tf))