"""
이름 : 황재찬
학번 : 2020039040
"""

list1, list2= [],[]
value=0

for i in range(0,4):
    for k in range(0,5):
        list1.append(value)
        value+=3
    list2.append(list1)
    list1 = []
    

for i in range(0,4):
    for k in range(0,5):
        print("%3d"% list2[i][k], end= ' ')
    print("")
    
