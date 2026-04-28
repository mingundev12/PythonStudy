#main1.py

# import calc
# import calc as c
# import calc 는 calc.py 전체사용

# 특정 함수나 변수를 사용하고자 한다면 아래와 같이 하면 된다.

# import 파일명
# import 파일명 as 별명
# from 파일명 import 함수명 as 별명
# from 파일명 import 함수명(변수명), 함수명, ...

from calc import add

print(calc.add(1, 2))