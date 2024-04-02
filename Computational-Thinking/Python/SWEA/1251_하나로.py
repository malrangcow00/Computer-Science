import sys
sys.stdin = open('input/1251.txt', 'r')

T = int(input())


def find_set(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find_set(parent[x])
        return parent[x]


def union(x, y):
    px, py = find_set(x), find_set(y)

    if px != py:
        if px < py:
            parent[py] = px
        else:
            parent[px] = py


for tc in range(1, T + 1):
    N = int(input())
    # 각 섬의 x 좌표
    island_x = list(map(int, input().split()))
    # 각 섬의 y 좌표
    island_y = list(map(int, input().split()))
    # 환경부담 머시기
    E = float(input())

    parent = [_ for _ in range(N + 1)]

    # 각 섬의 좌표와 환경부담 머시기를 담은 리스트
    eco = []
    for i in range(N):
        for j in range(i + 1, N):
            a = (island_x[i] - island_x[j])
            b = (island_y[i] - island_y[j])
            eco.append([i, j, E * (a ** 2 + b ** 2)])

    # 환경부담을 기준으로 소트
    eco.sort(key=lambda x: x[2])

    cnt = 0
    sum_eco = 0

    for i in range(len(eco)):
        if find_set(eco[i][0]) != find_set(eco[i][1]):
            if cnt == N:
                break
            cnt += 1
            sum_eco += eco[i][2]
            union(eco[i][0], eco[i][1])

    print(f'#{tc} {int(round(sum_eco, 0))}')