def dfs(v):
    global visited 
    print(v, end=' ')
    visited[v]=True
    for i in range(1,n):
        if graph[v][i]==1 and visited[i]==False:
            dfs(i)

n = 8
nums = list(map(int, input().split()))[::-1]
graph = [[0]*n for _ in range(n)]

while nums:
    v1 = nums.pop()
    v2 = nums.pop()
    graph[v1][v2] = graph[v2][v1] = 1

visited = [True] + [False] * (n-1)

dfs(1)


# def dfs(v):
#     global visited
#     print(v, end=' ')
#     visited[v] = True

#     for i in graph[v]:
#         if visited[i] == False:
#             dfs(i)


# N = 8
# input_text = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'

# tmp_arr = list(map(int, input_text.split()))
# tmp_arr = tmp_arr[::-1]
# graph = dict()
# visited = [False for _ in range(8)]

# for _ in range(8):
#     pn = tmp_arr.pop()
#     cn = tmp_arr.pop()

#     graph.setdefault(pn, [])
#     graph.setdefault(cn, [])
#     graph[pn].append(cn)

# dfs(1)
