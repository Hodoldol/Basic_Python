# 자료형을 확인하는 방법 : type()
print(type(100))
print(type("문자열"))
print(type(1.5))

# 문자열(str)
print("안녕하세요")
print('안녕하세요')
print("'안녕하세요' 반갑습니다.")

# 문자열에서 줄 바꾸는 방법
print("""안녕하세요.
문자열에서 줄을 바꿉니다.
""")

# 문자열 반복 연산자 : *
print("반복 " * 3)

# 문자열 인덱싱
print("안녕하세요"[1:4])
print("안녕하세요"[-3:-1])
print("안녕하세요"[1:])

# 문자열 길이 구하기 : len()
print(len("안녕하세요"))

# 숫자형(int,float)
print(type(123))
print(type(1.5))

# 사칙연산, 나머지 연산자
print(1+2)
print(1-2)
print(1*2)
print(1/2)
print(1//2)
print(1%2)
print(2**2)

# 변수
x = 12345
x + 1

# 복합 대입 연산자 : 기존의 연산자와 조합해서 사용할 수 있는 연산자
number = 100
number += 10
print(number)

# type 바꾸기 : str(), int(), float()
int_a = int("12")
float_a = float("12.56")
print(int_a, float_a)

string_a = input("숫자를 입력하세요.")
int_a = int(string_a)
print(type(int_a))

string_b = str(12)
print(type(string_b))