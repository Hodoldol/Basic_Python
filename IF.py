# Boolean : True와 False가 존재
print(True)
print(False)

# 비교 연산자
print(1 == 2)
print( 1 < 20)

# 논리 연산자 : not, and, or
print(not True)
print(True and False) # 두 값 모두 True여야 True
print(True or False) # 두 값 모두 False여야 False

# if 조건문
number = input("정수를 입력하세요.")
number = int(number)

if number >0:
    print("양수입니다.")

# else문 : 조건이 두 개
number = input("정수를 입력하세요.")
number = int(number)

if number % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")

# elif문 : 조건이 세 개 이상
number = input("정수를 입력하세요.")
number = int(number)

if number > 0:
    print("양수입니다.")
elif number < 0:
    print("음수입니다.")
else:
    print("0 입니다.")
