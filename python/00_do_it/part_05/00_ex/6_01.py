#외장함수--> 파이썬 라이브러리
#sys
import sys
print(sys.argv)
print("테스트는 영어로")

if False:
    sys.exit()#강제 프로그램 종료
    print("종료 후이므로 실행되지 않는 코드")

print("test")



#sys.argv: 명령어 프롬프트 창에서 명령어 뒤의 모든 것드 ㄹ이 공백을 기준으로 나뉘어서 sys.argv 리스트 요소가된다.