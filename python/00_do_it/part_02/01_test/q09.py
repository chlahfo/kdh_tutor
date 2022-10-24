#다음과 같은 딕셔너리 a 가 있다.
a=dict()
#오류가 발생하는 경우를 고르고 그 이류를 설명해보자.
#3번 list 는 key가 될 수 없음
a["name"]="python"
a[("a",)]="python"
a[250]="python"
print(a)