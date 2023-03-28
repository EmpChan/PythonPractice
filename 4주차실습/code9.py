"""
이름 : 황재찬
학번 : 2020039040
"""
import operator

trainDic, trainlist = {},[]

trainDic = {'Thomas' : '토마스',\
            'Edward' : '에드워드',\
             'Henry' : '헨리',\
            'Gothen' : '고든',\
            'James' : '제임스'}
trainlist = sorted(trainDic.items(),key = operator.itemgetter(0))

print(trainlist)

    
