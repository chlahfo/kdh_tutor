#time - 시간모듈
import time
print(time.time())#현재 시간을 실수 형태로  초단위로 돌려줌.

print(time.time())

print(time.localtime(time.time()))#time.time()의  초단위를 연, 월,일, 시, 분 ,초의 형태로 바꿔주는 함수

print(time.asctime(time.localtime(time.time())))# 튜플 형태의 값을 인수로 받아서 날짜 및 시간을 알아보기 쉬운 형태로 돌려주는 함수

print(time.ctime())#항상 지금 시간만을 표기

print(time.strftime("%x %X", time.localtime(time.time())))
print(time.strftime("%c", time.localtime(time.time())))

#time.sleep-> 일정한 시간 간격 루프 실행
for i in range(10):
    print(i)
    time.sleep(1)

print("테스트")# time.sleep 뒤에 있는 코드도 느리게 지연됨.