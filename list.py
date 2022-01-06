# 리스트(list) : 여러가지 자료를 저장할 수 있는 자료
# 리스트 내부에 넣는 자료를 요소라고 말합니다.
# 리스는 한 가지 자료형만으로도 구성할 수 있지만, 여러 자료형도 괜찮습니다.
list = [1, "안녕", 3, True, False]
print(list)
list[2] = 5
print(list)
list[0]
list[-1]
list[1:4]
list[1][0]

# 리스트 연산자
list_a = [1,2,3]
list_b = [4,5,6]
print(list_a + list_b)
print(list_a * 3)
print(len(list_a))

#### 리스트 관련 함수
# 요소 추가 : append, insert, extend
list_a = [1,2,3]
list_a.append(4)
print(list_a)
list_a.insert(2,10)
print(list_a)
list_a.extend([4, 5, 6])
print(list_a)

# 요소 제거 : del, pop, remove, clear
list_a = [1, 2, 3, 4, 5, 6]
del list_a[1]
print(list_a)
list_a.pop(2) 
print(list_a)
list_a.remove(5) # 값으로 제거, 중복된 값이 있으면 먼저 발견되는 것을 제거
print(list_a)
list_a.clear() # 리스트 내의 모든 요소를 제거

# 리스트 내부에 있는지 확인 : in/not in 연산자
list_a = [1, 2, 3, 4, 5]
3 in list_a
10 not in list_a

# for 반복문
for i in range(100):
    print("출력")
list = [1, 2, 3, 4, 5]
for element in list:
    print(element)

# 딕셔너리 : 키를 기반으로 값을 저장하는 형태
dict_a = {
    "name" : "호돌돌",
    "sex" : "male"
}
dict_a
dict_a["name"]

#### 딕셔너리 관련 함수
# 값 추가/제거
dict_a = {
    "name" : "호돌돌",
    "sex" : "male"
}
dict_a["age"] = "100"
dict_a["age"] = "30" # 기존에 존재하는 key에 값을 적을 경우 새로운 값으로 대치
del dict_a["age"]

# get(), in : 딕셔너리 내부에 키 존재 여부 확인
dict_a = {
    "name" : "호돌돌",
    "sex" : "male"
}

key = input("원하는 키:")
if key in dict_a:
    print(dict_a[key])
else:
    print("존재하지 않는 키입니다.")
print(dict_a.get("name"))
print(dict_a.get("age"))

# range() : 범위를 나타내는 함수
range(10) # 0~9
range(1, 10) # 1~9
range(1, 10, 2) # 1~9, 2만큼 차이

# while 반복문 : 조건이 Ture일 때 계속 진행(무한 반복)
i = 0 
while i < 10:
    print(i)
    i += 1

# break : 탈출, continue : 현재 반복을 생략하고 다음 반복으로 넘어감.
i = 0
while True:
    print("{}번째 반복".format(i))
    i += 1
    input_text = input("종료?(y/n)")
    if input_text in ["Y", "y"]:
        print("반복을 종료")
        break

numbers = [1, 10, 15, 5, 20]
for number in numbers:
    if number < 10:
        continue
    print(number)

