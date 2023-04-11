inFp = open("data.txt", "r")
while True:
    inStr = inFp.readline()
    if inStr == "":
        break
    print(inStr, end = "")

inFp.close()
