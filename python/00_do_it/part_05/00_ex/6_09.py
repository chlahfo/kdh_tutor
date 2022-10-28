#스레드를 다루는 모듈
#thread_test.py
import time 
def long_task():# 5초의 시간이 걸리는 함수
    for i in range(5):
        time.sleep(1)#1초 대기
        print("working %s\n" % i)
    
print("start")

for i in range(5):
    long_task()# 5초 함수 5번 실행 ==> 25초 걸림