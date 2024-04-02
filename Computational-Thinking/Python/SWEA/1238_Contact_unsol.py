import sys
sys.stdin = open('input/1238.txt', 'r')

def DFS(start, depth):
    global mx
    global history
    mx = max(mx, depth)
    for i in graph[start]:
        if not visited[i]:
            visited[i] = 1
            history[depth].append(i)
            history += [[]]
            DFS(i, depth+1)
            history.pop()

for tc in range(1, 11):
    N, start = map(int, input().split())
    data = list(map(int, input().split()))
    graph = [[] for _ in range(101)]
    for i in range(0, N-1, 2):
        graph[data[i]].append(data[i+1])
    history = [[]]
    visited = [0] * 101
    visited[start] = 1
    mx = 0
    DFS(start, 0)
    print(f'#{tc} {max(history[mx-1])}')