"""
이름 : 황재찬
학번 : 2020039040
"""

mine = [30,10,20]

mine.append(40)
print("append(40) gndml fltmxm : %s"%mine)

print("pop() 으로 추출한 값 : %s"% mine.pop())
print("pop() 후의 리스트 : %s"% mine)

mine.sort()
print("sort()후의 리스트 : ", mine)

mine.reverse()
print("reverse() 후의 리스트 : ",mine)

print("20값의 위치 : ",mine.index(20))

mine.insert(2,222)
print("inser(2,222) 후의 리스트 : ", mine)

mine.remove(222)
print("remove(222)후의 리스트 : ",mine)

mine.extend([77,88,77])
print("extend([77,88,77])후의 리스트 : ",mine)

print("77값의 개수 : ", mine.count(77))

