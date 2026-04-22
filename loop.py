# loop.py

# print("숫자 : 1")
# print("숫자 : 2")
# print("숫자 : 3")
# print("숫자 : 4")
# print("숫자 : 5")

# 5번 반복하는 반복문
for i in range(5,0,-1) :
    print("숫자 : " + str(i))



print("===================")

for ch in "hello" :
    print(ch)

for name in ["차도헌","박지연","이성찬","김진숙","이동렬","김현규"] :
    print(name)
    
total = 0
for i in range(1, 11) :
    total += i
print("총합 : " + str(total))

# Q2. ["15,000", "13,000", "8,700", "9,000", "25,000"]
# 배열에 출금금액 저장
# 10,000 이상 금액을 출력

money_list = ["15,000", "13,000", "8,700", "9,000", "25,000"]
for money_str in money_list :
    money = int(money_str.replace(",",""))
    if money >= 10000 :
        print(money_str)

for i in range(len(money_list)) :
    print("금액 : ", i, money_list[i])

for i, v in enumerate(money_list) :
    print(i, v.rjust(6))



# Q3. [89, 56, 78, 92, 61, 96, 83, 74]
# 203 호 학생들의 성적이다. 성적의 총합과 평균을 출력하세요
# 80점 이상인 학생들의 위치(인덱스)도 출력하세요

score = [89, 56, 78, 92, 61, 96, 83, 74]

print(f"총점 : {sum(score)}, 평균 : {sum(score) / len(score)}")

for i, v in enumerate(score) :
    if v >= 80 :
        print("80점 넘은 학생 : ", i)