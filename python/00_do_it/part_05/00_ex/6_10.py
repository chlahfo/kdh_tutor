#두번째 방법
import time
import threading

def long_task():    #5초 걸리는 함수
    for i in range(5):
        time.sleep(1)
        print("working%s\n" %i)

print("start")

threads=[]
for i in range(5):
    t = threading.Thread(target=long_task)# 스레드를 생성
    threads.append(t)#threads 배열에 스레드를 집어넣음.
for t in threads:
    t.start()#스레드를 실행

print("End")

#총 5초걸림다만, start 와 end 가 먼저 출력되어버림
