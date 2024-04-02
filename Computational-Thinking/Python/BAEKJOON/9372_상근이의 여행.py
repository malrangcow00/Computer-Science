import sys
input = sys.stdin.readline

def dfs(start):
    global cnt
    visited[start] = 1
    for i in nations[start]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    nations = [[] for _ in range(N+1)]
    for flight in range(M):
        a, b = map(int, input().split())
        nations[a].append(b)
        nations[b].append(a)

    visited = [0] * (N + 1)
    cnt = 0
    dfs(1)
    print(cnt)