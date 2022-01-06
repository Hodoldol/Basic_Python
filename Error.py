# SyntaxError(구문 오류) : 코드를 잘못 입력하지 않았는지 다시 확인
print(""안녕하세요. 구문 오류 입니다.")

# IndexError 1 : 리스트/문자열의 수를 넘는 요소/글자를 선택한 경우 발생
print("안녕하세요"[10])
list_a = [1, 2, 3]
list_a[3]

# IndexError 2 : {}의 개수가 format() 함수의 매개변수 개수보다 많으면 발생 
# 매개변수가 더 많을 경우 버려지는 대신 오류는 없음.
"{} {} {}".format(1, 2)
"{} {}".format(1, 2, 3, 4, 5)

# TypeError : 서로 다른 자료형끼리의 연산시 발생
string = "문자열"
number = 123
string + number

# ValueError : 자료형을 변환할 때 '변환할 수 없는 것'을 변환할 경우 발생
int("안녕하세요")
float("반가워요")
int("52.273")

# IndentationError : If구문과 같이 들여쓰기가 필요한 곳에서 사용하지 않은 경우 발생
if zero == 0:

else:
    

# raise NotImplementError : 아직 구현하지 않은 부분이에요!라는 오류

# NameError : 딕셔너리 내에 키를 지정할 때 식별자("",'')를 입력하지 않은 경우 발생
dict_a = {
    name : "이준호"
}

# KeyError : 리스트의 IndexError와 마찬가지로 딕셔너리에 존재하지 않는 key에 접급할 시 발생
dict_a = {
    "name" : "이준호"
}
dict_a["age"]
