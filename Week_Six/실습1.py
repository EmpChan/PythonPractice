"""
이름 : 황재찬
학번 : 2020039040
"""
def factorial(n:int)->int:
    if n>0:
        return n * factorial(n-1)
    else :
        return 1
    
if __name__ == '__main__':
    n = int(input('출력할 팩토리얼값을 입력하세요.: '))
    print(f'{n}의 팩토리얼은 {factorial(n)}입니다.')
