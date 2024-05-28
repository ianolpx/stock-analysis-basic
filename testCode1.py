
print("Hello world!")

# variable
a = 2
b = 3
c = a + b
print(c)

# booleans and strings
my_name = "minju" # 문자열 변수
age = 12
dead = False # True : 1, on, False : 0, off
print("Hello my name is", my_name)
print("and I'm ", age, " years old")

# function : 재사용 가능한 코드
# 함수 정의, 기본값 설정
def say_hello(user_name="anonymous", user_age=0): # 함수 이름, 매개변수
    print("hello", user_name) # 들여쓰기
    print("you are", user_age, "years old")

# 함수 호출
say_hello("nico", 12) # 함수 이름, 인자

# return : 함수의 결과값을 반환
def tax_calc(money):
    return money * 0.35

def pay_tax(tax):
    print("thank you for paying", tax)

# 함수 호출(1)
to_pay = tax_calc(1500000000000)
pay_tax(to_pay)

# 함수 호출(2)
pay_tax(tax_calc(1500000000000))
 
my_name = "minju"
my_age = 12
my_color_eyes = "brown"

# f-string
print(f"Hello I'm {my_name}, I have {my_age} years old, and my eyes are {my_color_eyes}")

# juice maker 만들기
def make_juice(fruit):
    return f"{fruit}+🥤"

def add_ice(juice):
    return f"{juice}+🧊"

def add_sugar(iced_juice):
    return f"{iced_juice}+🍬"

juice = make_juice("🍎")
cold_juice = add_ice(juice)
perfect_juice = add_sugar(cold_juice)

print(perfect_juice)

# if : 조건문, 참일 때 한번 실행
password_correct = True

if password_correct:
    print("Here is your money")
else: # 선택사항
    print("Wrong password")

# elif
winner = 10
if winner <= 10:
    print("If")
elif winner <= 25:
    print("elif")
elif winner == 0:
    print("elif 2")
elif winner == 50:
    print("elif 3")
else:
    print("Else")

# input : 입력값 받기
age = int(input("How old are you?")) # input은 문자열
print(type(age))

# and & or
if age < 18:
    print("You can't drink.")
elif age >=18 and age <= 35:
    print("You drink beer!")
elif age == 60 or age == 70:
    print("Birthday party!")
else:
    print("Go ahead!")


# standard library 함수 호출
from random import randint

# while : 조건이 참일 때 반복
pc_choice = randint(1, 100) # 1~100중 랜덤한 숫자

playing = True

while playing:
    user_choice = int(input("Choose number: (1-100)"))
    if user_choice == pc_choice:
        print("You won!")
        playing = False
    elif user_choice > pc_choice:
        print("Lower!")
    elif user_choice < pc_choice:
        print("Higher!")

