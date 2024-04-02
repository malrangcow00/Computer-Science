def find_set(x):  # x의 대표자(부모)가 누구인지
    if x == parent[x]:
        return x
    else:
        parent[x] = find_set(parent[x])  # 최적화 : 경로압축
        return parent[x]

def union(x, y):  # x 와 y 집합을 합칠 때
    px = find_set(x)
    py = find_set(y)

    if px != py:
        parent[px] = py

# n : 집합의 개수 + 1, m : 그 후의 연산의 개수
n, m = map(int, input().split())

# 집합 초기화 (make_set)
parent = [i for i in range(n + 1)]

# 연산 갯수 m개 만큼 입력 받아서 처리
for _ in range(m):
    oper, a, b = map(int, input().split())
    # 집합을 합치는 연산 '0' -> union
    if oper == 0:
        union(a, b)
    # 집합이 서로 같은지 확인 연산 '1' -> find
    elif oper == 1:
        if find_set(a) == find_set(b):
            print("YES")
        else:
            print("NO")