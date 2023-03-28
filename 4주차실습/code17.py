"""
이름 : 황재찬
학번 : 2020039040
"""

string = input("문자열 입력 : ")

checkalpha,checknum,elsething=0,0,0

for i in string:
    if i.isalpha():
        checkalpha=1
    elif i.isalnum():
        checknum=1
    else:
        elsething = 1

if elsething:
    print("모르겠습니다.")
else:
    if checkalpha and checknum:
        print("글자 + 숫자입니다.")
    elif checkalpha:
        print("글자입니다.")
    else:
        print("숫자입니다.")
