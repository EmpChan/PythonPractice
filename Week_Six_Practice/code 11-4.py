inFp = open("data.txt", "r")

inList = inFp.readlines()
for inStr in inList:
    print(inStr, end="")

inFp.close()
