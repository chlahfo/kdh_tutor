#리스트에 요소 추가(append)
a=[1,2,3]
a.append(4)
print(a)

a.append([5,6])
print(a)

#리스트 정렬(sort)
a=[0,23,78,5,6]#단, 숫자와 문자열 혼용해서 정렬 안됨
a.sort()
print(a)

b=["b","a","c", "ㅎ","ㅂ","ㄱ"]
b.sort()
print(b)

a.reverse()#순서대로 정렬후 역순 재생이 아닌 리스트를 그대로 뒤집음
print(a)
a.reverse()
print(a)
a.sort(reverse=True)#얘는 내림차순
print(a)

#위치 반환(index)
a=[1,2,3]
print(a.index(3))
print(a.index(1))# 문자열과 똑같이 해당 요소가 없는 경우 에러남


#리스트에 요소 삽입(insert)
a.insert(0,4) #0의 위치에 4 삽입
print(a)
a.insert(3,5)
print(a)

#리스트 요소 제거
a=[1,2,3,1,2,3]
a.remove(3)#여러개면 맨 처음 것만 삭제되고 뒤에는 그대로. 
print(a)

#리스트 요소 끄집어내기(pop) - 해당 요소 반환후 리스트에서 삭제
a=[1,2,3]
print(a.pop())
print(a)
a=[1,2,3]
print(a.pop(1))
print(a)

#리스트에 포함된 요소x의 갯수세기
a=[1,2,3,1]
print(a.count(1))

#리스트 확장(extend)
a=[1,2,3]
a.extend([4,5])
print(a)
b=[6,7]
a.extend(b)
print(a)

#???append 와 extend 차이점: 배열을 넣을 때 append 는 항목 그대로 넣어서 마지막 요소가 리스트가 됨. 반면 extend 는 확장되서 더하는 리스트의 요소가 그대로 더해짐. 마치 배열더하기처럼
