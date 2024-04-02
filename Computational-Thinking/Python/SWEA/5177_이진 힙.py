import sys
sys.stdin = open('input/5177.txt', 'r')
from heapq import heappush

T = int(input()) # 테스트 케이스 1 <= T <= 50

for tc in range(1, T+1):
    N = int(input()) # N: 주어지는 서로 다른 자연수의 개수, 5 <= N <= 500
    arr = list(map(int, input().split())) # 1,000,000 이하 N개의 수
    heap = []
    for num in arr:
        heappush(heap, num)
    # heap.insert(0, 0)
    heap = [0] + heap
    result = 0
    while N > 1:
        N //= 2
        result += heap[N]
    print(f'#{tc} {result}')