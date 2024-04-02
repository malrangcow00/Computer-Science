from heapq import *
from collections import deque

# 파이썬의 컬렉션들은 클래스...
# -> 자료형. 메소드로 사용o.
# dq = deque()
# dq.pop()

from random import randint

# 리스트를 하나 생성
heap = []
for i in range(10):
    heap.append(randint(1, 1000))

print(heap)

from heapq import heapify, heappop, heappush

# heap 자료구조에 맞게 변형 : heapify
heap = [-i for i in heap]

heapify(heap)
print(heap)

# heap에서 데이터를  뽑아낸다.
item = heappop(heap)
print(-item)
item = heappop(heap)
print(-item)
item = heappop(heap)
print(-item)
