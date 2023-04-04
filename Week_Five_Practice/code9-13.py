"""
이름:황재찬
학번:2020039040
"""

import random as rand

def getN():
    return rand.randrange(1,46)

lotto = []
print("** 로또 추첨을 시작합니다. **")

while len(lotto) < 6:
    k = getN()
    if k not in lotto:
        lotto.append(k)

lotto.sort()
print("추첨된 로또 번호 ==> ",end='')
for i in lotto:
    print(i,end=' ')
