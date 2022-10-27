#오류 회피하기
try:
    f=open("없는파일", "r")
except FileNotFoundError:
    pass