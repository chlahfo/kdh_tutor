#오류 일부러 발생시키기- raise 명령어 사용
class Bird:
    def fly(self):
        raise NotImplementedError

#자식 클래스가 fly 함수를 구현하지 않을 경우ㅡ메서드 오버라이딩 해야 에러가 발생하지 않음
a = Bird()
class Eagle(Bird):
    def fly(self):
        print("very fast")
eagle = Eagle()
eagle.fly()
