"""
이름 : 황재찬
학번 : 2020039040
"""
inFp = open("img1.gif","rb")
outFp = open("img99.gif", "wb")

while True:
    inStr = inFp.read(1)
    if not inStr:
        break
    outFp.write(inStr)

inFp.close()
outFp.close()
print("--- 이진파일이 정상적으로 복사되었음 ---")
