#여러줄 문자열

#이스케이프 \n사용(줄이 길어지고 읽기 불편)
txt1="Life is too short \nYou need Python"
print(txt1)

#연속된 작은 따홈표 3개 큰따옴표 3개(읽기 편함)
txt2='''
Life is too short
You need Python
'''
txt3='''


Life is too short
You need Python


'''
print(txt2, txt3)