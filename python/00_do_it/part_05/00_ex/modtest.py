#다른 파일에서 모듈 불러오기--> 동일한 디렉토리에 있어야 한다.
import mod2
result = mod2.add(3, 4)
print(result)

#다른 방법->대화영 인터프리터에서 sys.path.append 사용하기
#PYTHONPATH 환경 변수 사용
