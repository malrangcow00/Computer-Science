"""
stack = []
visited[]
dfs(v):
  visited[v] <- True
  while True:
    if v에 인접하고 방문안한 w가 있으면
      push(v)
      v <- w
      visited[w] <- true
    elif stack
      v <- pop()
    else
      break

"""

N = 7

# 방문 체크
visited = [False for _ in range(N)]
graphs = [
    [1, 2],  # 0
    [0, 3, 4],  # 1
    [0, 4],  # 2
    [1, 5],  # 3
    [1, 2, 5],  # 4
    [3, 4, 6],  # 5
    [5]  # 6
]


def dfs(v):
    global visited
    print(v, "-", end='')
    visited[v] = True
    # v 노드에서 갈 수 있는 노드를 확인 (인접한 노드)
    for u in graphs[v]:
        if visited[u] == True:  # 방문을 했다면
            continue
        # 방문을 하지 않았다면 방문을 진행
        dfs(u)


dfs(0)
