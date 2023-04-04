"""
이름 : 황재찬
학번 : 2020039040 
"""

def coffee_machine(but):
    print("\n#1. (자동으로) 뜨거운 물을 준비한다.");
    print("#2. (자동으로) 종이컵을 준비한다.")
    
    if but==1:
        print("#3. (자동으로) 아메리카노를 탄다.")
    elif but==2:
        print("#3. (자동으로) 카페라떼를 탄다.")
    elif but==3:
        print("#3. (자동으로) 카푸치노를 탄다.")
    elif but==4:
        print("#3. (자동으로) 에스프레소를 탄다.")
    else:
        print("#3. (자동으로) 아무거나 탄다.")

    print("#4. (자동으로) 물을 붓는다.")
    print("#5. (자동으로) 스푼으로 젓는다.\n")
    

button = int(input("로제손님 어떤 커피 드릴까요?(1:아메리카노, 2:카페라떼, 3:카푸치노, 4.에스프레소)"))
coffee_machine(button)
print("로제손님~ 커피 여기 있습니다.")

button = int(input("리사손님 어떤 커피 드릴까요?(1:아메리카노, 2:카페라떼, 3:카푸치노, 4.에스프레소)"))
coffee_machine(button)
print("리사손님~ 커피 여기 있습니다.")

button = int(input("지수손님 어떤 커피 드릴까요?(1:아메리카노, 2:카페라떼, 3:카푸치노, 4.에스프레소)"))
coffee_machine(button)
print("지수손님~ 커피 여기 있습니다.")1

button = int(input("제니손님 어떤 커피 드릴까요?(1:아메리카노, 2:카페라떼, 3:카푸치노, 4.에스프레소)"))
coffee_machine(button)
print("제니손님~ 커피 여기 있습니다.")
