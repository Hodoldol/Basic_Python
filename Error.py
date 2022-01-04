# Syntax Error(구문 오류) : 코드를 잘못 입력하지 않았는지 다시 확인
print(""안녕하세요. 구문 오류 입니다.")

# Index Error : 리스트/문자열의 수를 넘는 요소/글자를 선택한 경우 발생
print("안녕하세요"[10])

# Type Error : 서로 다른 자료형끼리의 연산시 발생
string = "문자열"
number = 123
string + number
