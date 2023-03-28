"""
이름 : 황재찬
학번 : 2020039040
"""

from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    for i in range(len(a)):
        if a[i] == key:
            return i
    return -1

arr = [1,2,3,4,5,6]
print("3의 위치 : ", seq_search(arr,3))
