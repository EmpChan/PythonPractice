"""
이름 : 황재찬
학번 : 2020039040
"""
inFp = open("data.txt","r")
outFp = open("data2.txt", "w")

inList = inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print("--- 파일이 정상적으로 복사되었음 ---")
