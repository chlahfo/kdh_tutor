#여러 개의 오류 처리
# ZeroDivisionError가 발생하여 IndexError가 발생하지 않는다.
try:
    a = [1,2]
    print(a[3])
    print(4 / 0)
except ZeroDivisionError:
    print("0 으로 못나눔")
except IndexError:
    print("인덱싱 안됨")

#아래와 같이 한꺼번에 쓸 수 있다.
try:
    a = [1,2]
    print(a[3])
    print(4 / 0)
except (ZeroDivisionError, IndexError) as e:
    print(e)