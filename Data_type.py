#### 자료형을 확인하는 방법 : type()
print(type(100))
print(type("문자열"))
print(type(1.5))

#### 문자열(str)
print("안녕하세요")
print('안녕하세요')
print("'안녕하세요' 반갑습니다.")

#### 문자열에서 줄 바꾸는 방법
print("""안녕하세요.
문자열에서 줄을 바꿉니다.
""")

#### 문자열 반복 연산자 : *
print("반복 " * 3)

#### 문자열 인덱싱
print("안녕하세요"[1:4])
print("안녕하세요"[-3:-1])
print("안녕하세요"[1:])

#### 문자열 길이 구하기 : len()
print(len("안녕하세요"))

#### 숫자형(int,float)
print(type(123))
print(type(1.5))

#### 사칙연산, 나머지 연산자
print(1+2)
print(1-2)
print(1*2)
print(1/2)
print(1//2)
print(1%2)
print(2**2)

#### 변수
x = 12345
x + 1

#### 복합 대입 연산자 : 기존의 연산자와 조합해서 사용할 수 있는 연산자
number = 100
number += 10
print(number)

#### type 바꾸기 : str(), int(), float()
int_a = int("12")
float_a = float("12.56")
print(int_a, float_a)

string_a = input("숫자를 입력하세요.")
int_a = int(string_a)
print(type(int_a))

string_b = str(12)
print(type(string_b))

#### 문자열의 여러 함수
a = "Hello Basic Python"
a.upper()
a.lower()
# isOO() : 구성을 파악하는 함수 -> isalnum, isdigit, isupper 등 종류 다양
print("10".isdigit()) 
# find() : 문자열 내부에 특정 문자 위치 확인(왼 -> 오)
x = "안녕안녕하세요".find("안녕")
print(x)
# 오 -> 왼
y = "안녕안녕하세요".rfind("안녕") 
print(y)
# in 연산자 : 문자열 내부에 문자열이 있는지 확인
print("안녕" in "안녕하세요") 
# split() : 문자열 자르기
a = " 10 20 30 40 50".split(" ")
print(a)

#### 문자열의 format() 함수
string_a = "{}".format(10)
print(string_a)
print(type(string_a))

format_a = "{}억 만들고 은퇴하고 싶다.".format(100)
format_b = "{} {} {}".format(1, "문자열", True)
print(format_a)
print(format_b)

#### format()을 이용한 숫자 출력
# 정수
a = "{:d}".format(12)
print(a)
a = "{:5d}".format(12)
b = "{:05d}".format(12)
print(a, b)

# 소수
a = "{:f}".format(12.345)
b = "{:10f}".format(12.345) # 10칸 만들기
c = "{:10.1f}".format(12.345) # 10칸 만들며, 소수점 1자리
print(a, b, c)