import sys
sys.stdin = open('SWEA.input/4871.txt', 'r')

T = int(input())
 
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj = [list(map(int, input().split())) for _ in range(E)]
    start, end = map(int, input().split())
 
    graphs = [[] for _ in range(V + 1)]
 
    visited = [False for _ in range(V + 1)]
 
    for idx in range(len(adj)):
        u = adj[idx][0]
        v = adj[idx][1]
 
        graphs[u].append(v)
 
    result = []
    def dfs(v):
        global visited
        result.append(v)
         
        visited[v] = True
        for u in graphs[v]:
            if visited[u] == True:
                continue
 
            dfs(u)
 
    dfs(start)
    if start in result and end in result:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')