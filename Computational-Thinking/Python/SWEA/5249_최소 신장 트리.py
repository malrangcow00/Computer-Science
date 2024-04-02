import sys
sys.stdin = open('input/5249.txt', 'r')

# 5249. 최소 신장 트리
'''
크루스칼 알고리즘 : 서로소 집합 자료구조 때 활용한 Union, Find 연산, 사이클 판별 로직을 활용하여 구현

크루스칼 알고리즘의 동작 과정
1. 모든 간선 정보에 대해 (오름차순)으로 정렬을 수행
2. 현재의 간선이 노드들 간의 사이클을 발생시키는지 확인
3. 만약 사이클이 발생하지 않은 경우(부모 노드가 다른 경우), 최소 신장 트리에 포함
'''

# find 연산 : x노드의 루트 노드를 찾아서 반환
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

#  union 연산 : 노드 a와 노드 b가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())

    # 부모 테이블 초기화
    parent = [0] * (V+1)
    for i in range(1, V+1):
        parent[i] = i

    # 간선 정보를 담을 리스트
    # 최소 신장 트리를 구성하는 간선의 가중치를 모두 더함 : total
    edges = []
    total = 0

    # 간선 정보를 입력받고 가중치를 기준으로 오름차순으로 정렬...
    for _ in range(E):
        a, b, w = map(int, input().split())
        edges.append((w, a, b))

    edges.sort()

    # 간선 정보 하나씩 확인하면서 크루스칼 알고리즘 수행
    for i in range(E):
        w, a, b = edges[i]
        # find 연산 후, 부모노드가 다르면 사이클 발생이 안하므로 union 연산 수행(최소 신장 트리에 포함)
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            total += w

    print(f'#{tc} {total}')