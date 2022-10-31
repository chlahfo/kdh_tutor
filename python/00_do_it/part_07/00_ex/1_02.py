#책으로
#정규표현식 없이 주민번호 뒷자리
data="""
park 800905-1049118
kim 800905-1049118
"""

result = []
for line in data.split("\n"):
    word_result=[]
    #공백마다 문자 나누기
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word=word[:6]+"-"+"*******"
        word_result.append(word)
    #나눈 단어 조립
    result.append(" ".join(word_result))
print("\n".join(result))
