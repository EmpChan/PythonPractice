"""
이름 : 황재찬
학번 : 2020039040
"""

inpstr=input("날짜(연/월/일) 입력 ==> ")

slist=inpstr.split('/')
print("입력한 날짜의 10년 후 ==> ",end ='')
print(str(int(slist[0])+10)+"년",end = ' ')
print(slist[1]+'월'+slist[2]+'일')
