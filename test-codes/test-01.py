# hello world 출력
print("hello world")

# "helo world" 출력
print("\"hello world\"")

# hello world 줄바꿔 3번 출력
print("hello world \n" * 3)

# .format 함수 사용
print("{}대학교 {}학과" .format("한서", "컴퓨터"))

# f-string
print(f"{1} + {2} = {1 + 2}")

# 함수 출력


def ex():
    print("hello")


ex()

# 함수에 변수
def ex1(ax):
  print(f"{ax} world")


ex1("hello")

# 함수 return


def ex2():
  return "hello world"


ex2()

# 조건절 if
age = 20

if age < 20:
  print("청소년")

if age >= 20:
  print("성인")

# 조건절 if elif else
age = 43

if age < 20:
  print("청소년")

elif age < 30:
  print("20대")

else:
  print("30~대")

# 반복문 while 1~10
i = 1

while i <= 10:
    print(i)
    i += 1

# while문으로 구구단 2단 출력
dan = 2
print(f"=={dan}단==")

i = 1
while i < 10:
    print(f"{dan} * {i} = {dan * i}")
    i += 1

# while문으로 구구단 2단~9단 출력
dan = 2
while dan < 10:
    print(f"=={dan}단==")

    i = 1
    while i < 10:
        print(f"{dan} * {i} = {dan * i}")
        i += 1
    dan += 1
