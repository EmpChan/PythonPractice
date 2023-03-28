"""
이름 : 황재찬
학번 : 2020039040
"""

string = input("입력 문자열 ==> ")
print("출력 문자열 ==> ", end ='')

if not string.startswith('('):
    print('(',end='')

print(string,end='')

if not string.endswith(')'):
    print(')',end='')
    
