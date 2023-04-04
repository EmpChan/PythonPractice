"""
이름 : 황재찬
학번 : 2020039040 
"""

def calc(v1,v2,op):
    if op == '+':
        return v1+v2
    elif op == '-':
        return v1-v2
    elif op == '*':
        return v1*v2
    elif op == '/':
        if v2==0:
            return "NO"
        return v1/v2
    elif op == '**':
        return v1**v2

v1 = int(input("첫 번째 수를 입력하세요. : "))
oper = input("계산을 입력하세요.(+,-,*,/,**) : ")
v2 = int(input("두 번째 수를 입력하세요. : "))
result = calc(v1,v2,oper)
if result=="NO":
    print("0으로는 나누면 안 됩니다.")
else:
    print("## 계산기 :",v1,oper,v2,'=',result)
