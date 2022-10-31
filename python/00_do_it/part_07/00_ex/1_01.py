#주민번호 뒷자리 *로 바꾸기
#정규 표현식 사용하지 않았을 때
#혼자 해보기
data="""
park 800905-1049118
kim 700905-1059119
choi 995015-2910570
i 901215-2903710
"""
aaa = data.split("\n")
aaa = list(filter(lambda x: x, aaa))
aaa = " ".join(aaa)
aaa = aaa.split(" ")
bbb=[]
for i in range(1, len(aaa), 2):
    aaa[i]= aaa[i].split("-")
    aaa[i][1]=aaa[i][1][0]+"******"
    aaa[i]="-".join(aaa[i])
    m_info = aaa[i-1] + " " + aaa[i]
    bbb.append(m_info)
bbb="\n".join(bbb)
print(bbb)
