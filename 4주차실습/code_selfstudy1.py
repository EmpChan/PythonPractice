"""
이름 : 황재찬
학번 : 2020039040
"""

numlist=[]
summation = 0
for i in range(1,11):
    numlist.append(int(input(str(i)+"번째 숫자 : ")))
    summation+=numlist[i-1]

print("합계 ==> ",summation)
