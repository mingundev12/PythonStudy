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

snack = dict()
for i, name in enumerate(snackName) :
    snack[name] = price[i]

print(snack)

snack2 = {k : price[i] for i, k in enumerate(snackName)}

print(snack2)

snack3 = {name : p for name, p in zip(snackName, price)}

print(snack3)