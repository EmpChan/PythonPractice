
"""
이름 : 황재찬
학번 : 2020039040
"""
import os

fName = input("파일명을 입력하세요 : ")

if os.path.exists(fName):
    inFp = open(fName, "r")

    inList = inFp.readlines()
    for inStr in inList:
        print(inStr, end="")
    
    inFp.close()
else:
    print("%s 파일이 없습니다."% fName)