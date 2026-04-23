#dataType.py

#리스트, 튜플
# list = 여러 데이터를 저장 관리하기 위한 파이썬 자료구조이다.
# tuple = 리스트와 유사하지만 리스트는 수정이 가능한 반면에 튜플은 수정이 불가능하다.

#리스트
number = [10, 20, 30, 40, 50]
empty = []
name = list()

print(number[0])
print(number[-5])


#리스트 자르기
num = number[2:4]
# print(number[0:1], num)

num2 = number[:3]
# print(num2, number[2:])

for i in range(len(number) + 1) :
    print(number[:i], number[i:])


#리스트 수정
number[2] = 100
print(number)


#리스트 추가
number.append(60) #리스트의 마지막 인덱스 다음에 추가
print(number)

number.insert(2, 500) #리스트의 원하는 위치에 추가(인덱스, 값)
print(number)

#리스트 값 삭제
number.remove(10) # 리스트에서 삭제할 데이터를 입력 (인덱스 X)
print(number)

number.pop(3) # 리스트에서 삭제할 데이터의 인덱스를 입력
print(number)

del number[2] # 인덱스로 삭제
print(number)

#리스트 크기(길이)
print(len(number))

print("----------")
for num in number :
    print(num)

for i, num in enumerate(number) :
    print(i, num)

# 리스트 검색
print(40 in number) # 값의 존재여부 True, False
print(number.index(50)) # 인덱스 찾기, 없으면 오류

# index를 통해 인덱스를 찾기 전에 in 으로 존재여부 확인 먼저 하기

# 리스트 정렬
number.sort()
print(number)
number.sort(reverse=True)
print(number)
