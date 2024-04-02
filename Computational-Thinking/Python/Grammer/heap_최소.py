# 최소힙 구현 (라이브러리 heapq 사용해서...!)
from heapq import heappop, heappush, heapify

# 우선순위 큐... 값이 가장 작은 값을 꺼내고 넣는 과정...
heap = [] # 비어있는 리스트
heappush(heap, 90)
heappush(heap, 40)
heappush(heap, 30)
heappush(heap, 90)
heappush(heap, 100)
print(heap)

item = heappop(heap)
print(item)
print(heap)