"""
이름 : 황재찬
학번 : 2020039040
"""
def recur(n: int) -> int:
    while n>0:
        recur(n-1)
        print(n)
        n=n-2

if __name__ == '__main__':
    recur(5)#이건 내가임의로넣은 테스트코드 생략부분임
    
