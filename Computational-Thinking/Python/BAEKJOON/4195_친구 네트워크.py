import sys
input = sys.stdin.readline

def make_set(N):  # 각 요소를 부모로 자기 자신을 초기화
    # 초기화를 진행한다... (각 요소를 자기자신으로 초기화 진행)
    parent = [j for j in range(N + 1)]
    return parent

def find_set(x):  # 요소 x에 대해서 대표자(부모)를 찾아서 반환..
    # 자기 자기 자신을 가리키는 노드라면 자신을 반환 (대표자)
    if x == parent[x]:
        return x
    else:
        parent[x] = find_set(parent[x]) # 최적화 : 경로 압축
        return parent[x]

def union(x, y):  # 요소 x, y 속해있는 두개의 그룹을 하나로 통합..
    px = find_set(x)
    py = find_set(y)

    if px != py:
        parent[py] = px
        cnt[x] += cnt[y]

for _ in range(int(input())):
    num = int(input())
    parent = {}
    cnt = {}
    for i in range(num):
        x, y = input().split()
        if x not in parent:
            parent[x] = x
            cnt[x] = 1
        if y not in parent:
            parent[y] =y
            cnt[y] = 1
        union(x, y)
        print(cnt[x])