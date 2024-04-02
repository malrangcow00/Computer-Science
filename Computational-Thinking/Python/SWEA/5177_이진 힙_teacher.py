import sys
sys.stdin = open('input/5177.txt', 'r')

from heapq import heappush

# 이진힙
T = int(input())
for tc in range(1, T + 1):
    # 입력
    # 노드의 개수 N
    N = int(input())
    # 노드들의 값
    nodes = list(map(int, input().split()))

    # 로직
    # 최소힙에다가 N개의 노드들을 하나씩 삽입하여 힙을 완성 시킨다...
    heap = []  # 힙으로 사용할 빈 리스트...
    for i in range(N):
        heappush(heap, nodes[i])
    # 첫 원소를 아무거나 임시값으로 부여 (인덱스 0을 사용하지 않기 하기 위해)
    heap = [0] + heap
    # 출력
    # 마지막 노드에서 루트 노드까지의 합을 출력한다.
    total = 0
    # 자식 인덱스 // 2 => 부모 인덱스
    p = len(heap) - 1
    while p > 0:
        p = p // 2  # 부모 노드로 이동한다
        total += heap[p]  # 현재 노드의 값을 더해주고

    print(f"#{tc} {total}")