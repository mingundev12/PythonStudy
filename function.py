# function.py

# 제어자 반환타입 메서드이름 (매개변수)

# 파이썬 함수 - def 함수이름 (매개변수) :


def intro(name : str) :
    print(name, "님 로그인 하셨습니다")



name = "김유신"

if type(name) == str:  #isinstance(name, str)
    intro(name)


intro("하늘소")
intro("감기약")
intro(1000)


def dataInput(a, b, c) :
    print(a + b + c)

dataInput(1, 20, 30)