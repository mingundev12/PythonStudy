# loop.py

# print("숫자 : 1")
# print("숫자 : 2")
# print("숫자 : 3")
# print("숫자 : 4")
# print("숫자 : 5")

# 5번 반복하는 반복문
# for i in range(5,0,-1) :
#     print("숫자 : " + str(i))



# print("===================")

# for ch in "hello" :
#     print(ch)

# for name in ["차도헌","박지연","이성찬","김진숙","이동렬","김현규"] :
#     print(name)
    
# total = 0
# for i in range(1, 11) :
#     total += i
# print("총합 : " + str(total))

# # Q2. ["15,000", "13,000", "8,700", "9,000", "25,000"]
# # 배열에 출금금액 저장
# # 10,000 이상 금액을 출력

# money_list = ["15,000", "13,000", "8,700", "9,000", "25,000"]
# for money_str in money_list :
#     money = int(money_str.replace(",",""))
#     if money >= 10000 :
#         print(money_str)

# for i in range(len(money_list)) :
#     print("금액 : ", i, money_list[i])

# for i, v in enumerate(money_list) :
#     print(i, v.rjust(6))



# # Q3. [89, 56, 78, 92, 61, 96, 83, 74]
# # 203 호 학생들의 성적이다. 성적의 총합과 평균을 출력하세요
# # 80점 이상인 학생들의 위치(인덱스)도 출력하세요

# score = [89, 56, 78, 92, 61, 96, 83, 74]

# print(f"총점 : {sum(score)}, 평균 : {sum(score) / len(score)}")

# for i, v in enumerate(score) :
#     if v >= 80 :
#         print("80점 넘은 학생 : ", i)


# 반복문 while

# while 조건 :
#     실행코드

#while 문은 조건식이 참인 경우에 동작하기때문에
#쉽게 무한루프에 들어갈 수 있다.
#하여 while문 사용 시 중단시킬 수 있는 break를 같이 사용하는 게 좋다.

# num = 5
# while num > 2 :
#     print("2보다 크다")
#     break


# while True :
#     num += 1
#     if num == 7 : continue
#     print(num)
#     if num == 10 : break

# print("=======")

# while True :
#     cmd = input("명령어 입력 : ").strip().lower()
#     if cmd == "history" :
#         print("모든 기록 출력")
#     elif cmd == "mkdir" :
#         print("새로운 폴더 만들기")
#     elif cmd == "remove" :
#         print("파일 삭제")
#     elif cmd == "exit" : 
#         print("종료")
#         break
#     else :
#         print("존재하지 않는 명령어 입니다.")


# 파이썬 랜덤 사용
import random

# num = random.randint(1, 10)
# print(num)

# 동전 앞면 뒷면 맞추기 게임 만들기

# coin = random.randint(1, 2)
# while True :
#     answer = input("앞면 = 1 뒷면 = 2 입력하시오 : ").strip().lower()
#     if answer.isdigit() :
#         answer_num = int(answer)
#         if answer_num == coin :
#             print("정답!")
#             break
#         else :
#             print("틀렸습니다. 다시 도전하세요.")
#     else :
#         print("잘못된 입력입니다")


game = ["가위","바위","보"]
n = random.choice(game)
print(n)

# 가위바위보 게임 5판 진행
# 5번째 게임이 끝나면 몇승 몇패 몇무인지 출력

win = 0
lose = 0
draw = 0
while True :
    com = random.choice(game)
    player = input("가위바위보 : ").strip().lower()
    if player not in game :
        print("잘못된 입력입니다")
        continue
    diff = (game.index(com) - game.index(player)) % 3
    if diff == 0 : 
        print("당신 : ", player, "상대 : ", com, " 무승부")
        draw += 1
    elif diff == 1 : 
        print("당신 : ", player, "상대 : ", com, " 패배")
        lose += 1
    else : 
        print("당신 : ", player, "상대 : ", com, " 승리")
        win += 1
    if win + lose + draw >= 5 : break

print("win : ", win, " draw : ", draw, " lose : ", lose)