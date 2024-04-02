import sys
sys.stdin = open('input/5102.txt', 'r')

def bfs(s):
    q = []
    q.append(s)
    while q:
        current = q.pop(0)
        for i in graphs[current]:
            if distance[i] == 0:
                distance[i] = distance[current] + 1
                q.append(i)


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    graphs = [[] for _ in range(V + 1)]
    for i in range(len(arr)):
        graphs[arr[i][0]].append(arr[i][1])
        graphs[arr[i][1]].append(arr[i][0])

    distance = [0] * (V + 1)
    bfs(S)

    print(list(enumerate(graphs)))
    print(list(enumerate(distance)))
    print(f'#{tc} {distance[G]}')