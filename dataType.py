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

number.pop(3) # 리스트에서 삭제할 데이터의 인덱스를 입력 => 해당하는 인덱스의 값을 직접적으로 삭제하는 방법
print(number)

del number[2] # 인덱스로 삭제 => number[2] 라는 참조 변수를 삭제함으로써 number[2]라는 변수와 연결된 실제 값과의 연결을 끊음
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

# 리스트는 일반적으로 많이 사용되는 자료구조다.
# 자바에서 List(ArrayList)를 많이 사용한다면 파이썬은 리스트이다.
# 여러 데이터를 저장할 수 있고, 수정, 추가 가능하고, 반복문 사용 쉽고,
# 정렬, 검색도 되고 그래서 사용하기 좋은 것이다.


#리스트 문제 풀기
# q1. 5명의 이름이 저장되어 있는 리스트 만들기
# 5명의 이름 출력하는 반복문 만들기

names = ["이순신", "강감찬", "이성계", "문익점", "한석봉"]

print(type(names))
for name in names :
    print(name)


# q2. 정도전 이름을 추가하고 출력하세요
names.append("정도전")
print(names)


# q3. 리스트에 김유신이 있는지 확인하는 코드 작성하기

name = "김유신"
if name in names :
    print(name, "있다")
else :
    print(name, "없다")


# q4. 이름 리스트에 내림차순으로 정렬하여 출력하세요
names.sort(reverse=True)
print(names)

# q5. 과일의 이름이 두글자인 과일만 출력하세요

fruits = ["사과", "바나나", "파인애플", "딸기", "오렌지", "포도", "배"]

for fruit in fruits :
    if len(fruit) == 2 :
        print(fruit)

fruits.sort(key=len)

# q6. 과일 검색 프로그램 만들기
# 과일이름 키보드를 통해 입력받는다
# 입력한 과일이 리스트에 있다면 판매중, 없다면 품절 이라고 출력

# fruit = input("과일 이름 입력 : ").strip()
# if fruit in fruits :
#     print("판매 중")
# else :
#     print("품절")


# q7. 
# fruits.sort()
# print(fruits)
# price = [5000, 8000, 12000, 9500, 15500, 20400, 9000]
# buyFruits = input("과일 이름 입력 : ").strip()
# buyCounts = input("구매할 개수 입력 : ").strip()
# buyFruitList = buyFruits.split(" ")
# buyCountList = buyCounts.split(" ")

# total = 0
# for i, buyFruit in enumerate(buyFruitList) :
#     if buyFruit in fruits :
#         total += price[fruits.index(buyFruit)] * int(buyCountList[i])

# print("총 가격 : ", total)


# fruit_dict = dict(zip(fruits, price))

# buy_names = input("과일 이름 입력 : ").strip().split()
# buy_counts = [int(c) for c in input("구매할 개수 입력 : ").strip().split()]

# total = sum(fruit_dict[name] * count for name, count in zip(buy_names, buy_counts))

# print("총 가격 : ", total)








# tuple - 리스트처럼 여러 데이터를 저장할 수 있는 자료형이다.
# 저장한 데이터를 수정할 수 없다.
# 데이터를 보호하기 위한 목적
# 속도와 메모리 효율성

# dictionary 의 key 로 사용
# 여러개의 값을 반환(return) 시킬 때

# 튜플 만들기
number = (10, 20, 30, 40) # 작은괄호 - 튜플, 대괄호 - 리스트

print(number)
print(type((1,2,3,4))) # tuple
print(type((10))) # int
print(type((10,))) # tuple


# number[0] = 100 값 수정은 오류
print(number[1]) # index = 0 부터

# tuple 슬라이싱
print(number[1:3])

print(10 in number)
print(number.index(20))

# 리스트와 다른점
# 수정불가
# number.append(200) 오류
# number.remove(20) 오류
# number.pop(20) 오류
# del number[2] 오류

print(number.count(20)) # 특정값 개수 구하기

data = 10,20,30,40,50 # 패킹 - 여러값을 하나로 묶기
print(type(data))
print(data)

a, b, c, d, e = data # 언패킹 - 묶여있는 값을 여러 개로 나누기
print(a, b, c, d, e)

red = 20
blue = 10

red, blue = blue, red # 패킹과 언패킹을 동시에 진행 => 서로 다른 두 변수의 값을 변경하는 것이 가능
print(red, blue)

# 함수 반환 여러개
def get() :
    return 10,20,30,40

print(get())

# list <-> tuple
info = ("다음주", "금요일", "빨간날", "그래서", "우리는", "5월6일에", "봐요")

info_list = list(info)
info_list[0] = "이번주"

info = tuple(info_list)
print(info)