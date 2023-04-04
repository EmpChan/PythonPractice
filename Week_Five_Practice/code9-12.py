"""
이름:황재찬
학번:2020039040
"""

def para_func(*para):
    r=0
    for n in para:
       r+=n
    return r

print("매개변수가 2개인 함수를 호출한 결과 ==>",para_func(10,20))
print("매개변수가 3개인 함수를 호출한 결과 ==>",para_func(10, 20, 30))
