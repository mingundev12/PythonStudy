#dataType2.py

# dictionary
# dictionary 는 data를 key 와 value로 저장하는 자료형

info = {
    "name" : "이순신",
    "age" : 20, 
    "job" : "군인", 
    "email" : "hahaha@naver.com",
    "address" : "대전광역시 선화동 방산빌딩 2층 203호"
    }

print(info["name"])


# 딕셔너리는 언제 사용하는가?
# 로그인 회원이나, 상품정보, 단일게시글 정보, 설정값
# JSON 데이터, API 응답데이터용

mem = dict()

print(info.get("city"))

info["city"] = "대전"

print(info)

city = info.pop("city") # 딕셔너리 삭제(잘라내기)
print(city)
print(info)
del info["age"] # 딕셔너리 삭제
print(info)

if "name" in info :
    if info["name"] == "이순신" :
        print("이순신이다.")
    else :
        print("이순신이 아니다.")
else :
    print("이름 정보가 없습니다.")

# 이메일의 도메인은 무엇인가?

if "email" in info :
    email = info["email"]

    # 스플릿을 이용한 방법
    # domain = email.split("@")[1]
    # print(domain)

    # 슬래시를 이용한 방법
    domain = email[email.index("@") + 1:]
    print(domain)

# 주소가 잘못 저장 되었다. 선화동 아니고 대흥동이다. 수정하시오

if "address" in info :
    addr = info["address"]
    addr = addr.replace("선화동", "대흥동")
    info["address"] = addr

print(info)



nums3 = [i for i in range(1, 16) if i % 3 == 0]
print(nums3)

cost = [4500, 6700, 3100, 5800, 2700, 4900]

#cost 리스트에는 상품의 가격이 저장되어 있다.
# 5000원 이하는 저가형, 5000원 초과는 고가형 상품 이라고 저장하시오

result = ["저가형" if p <= 5000 else "고가형" if p <= 6000 else "초고가형" for p in cost ]

print(result)



# 학생 성적 관리 프로그램 만들기, 과목 국어 수학 영어
std1 = [89, 56, 73]
std2 = [45, 87, 35]
std3 = [81, 85, 94]
std4 = [90, 34, 61]
std5 = [59, 63, 70]

stdName = ["이순신", "임꺽정", "한석봉", "정약용", "김춘추"]
subject = "국어", "수학", "영어"

std = std1, std2, std3, std4, std5



score = dict()
for i, name in enumerate(stdName) :
    temp = dict()
    for j, cname in enumerate(subject) :
        temp[cname] = std[i][j]

    score[name] = temp


print(score)


# 문제1 . 딕셔너리를 만드세요

snackName = ["새우깡", "칙촉", "마가렛", "짱구", "포카칩", "초코하임"]
price = [2000, 3200, 4500, 3000, 2800, 4200]

# snack = dict()
# for i, name in enumerate(snackName) :
#     snack[name] = price[i]

# print(snack)

snack2 = {k : price[i] for i, k in enumerate(snackName)}

print(snack2)

# snack3 = {name : p for name, p in zip(snackName, price)}

# print(snack3)


# 문제 2. 딕셔너리를 만들고 다음 조건으로 조회하세요
item = ["선풍기", "냉장고", "에어컨", "Tv", "컴퓨터", "노트북", "청소기"]
brand = ["LG", "삼성", "LG", "삼성", "HP", "DELL", "다이슨"]
price = [80000, 1250000, 850000, 1540800, 2300000, 1570000, 534000]

#item, brand, price 의 각 인덱스 매칭이다.
#선풍기는 LG 이고 금액은 80000 원 이다
#딕셔너리의 키는 제품명 value는 브랜드와 금액
# 삼성 브랜드의 제품명과 금액을 출력하세요

items = {name : {"brand" : brand[i], "price" : price[i]} for i, name in enumerate(item)}

# print(items)

# for i in items :
#     if items[i]["brand"] == "삼성" :
#         print(i, items[i]["price"])


for name, info in items.items() :
    if info["brand"] == "삼성" :
        print(name, info["price"])



# set 중복허용X 순서X 자료형

data = {1, 2, 3, 4, 5, 3, 4, 5, 3, 4, 5}
print(data)

set1 = set()

list = ["이순신", "김춘추", "장영실", "이순신", "장영실"]

set2 = set(list)
print(set2)

set2.add("한석봉")
print(set2)

set2.update(["정약용", "문익점", "이성계"]) # 여러 개 추가
print(set2)

set2.remove("한석봉") # 삭제 없는 것 삭제하면 오류
print(set2)

set2.discard("한석보") # 삭제 없어도 오류 없음
print(set2)


# set 안에 값이 존재하냐 -> in

# 교집합, 합집합, 차집합
a = {"복숭아", "배", "메론", "체리", "포도"} # 도헌이가 좋아하는 과일
b = {"사과", "배", "딸기", "바나나"} # 찬용이가 좋아하는 과일
c = {"바나나", "참외", "사과", "귤", "포도", "딸기", "토마토"} # 현규가 좋아하는 과일

print(a & b) # 교집합(∩)
print(a | c) # 합집합(∪)
print(b - c) # 차집합
print(b ^ c) # 대칭 차집합 (XOR)


"""
    list = 다수의 데이터 저장용으로 많이 사용, 중복 허용, 추가수정삭제 가능
    tuple =  다수의 데이터 저장 가능, 중복 허용, 추가수정삭제 불가능
    dict = key : value 구조, key는 중복안됨
    set = 중복허용 X 순서없ㅇ므, 검색, 그룹(집합)에 사용
"""

while True :
    menu = input("메뉴 선택 : ").strip()

    if menu == "1":
        print("목록")
        for fruit in fruits :
            print(f"{fruit['name']} / 가격 : {fruit['price']}원 / 재고 : {fruit['stock']}개")
    elif menu == "2" :
        print("검색")
    elif menu == "3" :
        print("판매")
    elif menu == "4" :
        print("재고")
    elif menu == "5" :
        print("추천")
    elif menu == "6" :
        print("기록")
    elif menu == "0" :
        print("종료")
        break
    else :
        print("잘못된 메뉴입니다")