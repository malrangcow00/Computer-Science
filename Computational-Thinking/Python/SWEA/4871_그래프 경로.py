import sys
sys.stdin = open('SWEA.input/4871.txt', 'r')

T = int(input())

def dfs(s):
  # 전역 변수 설정 : 필수가 아니더라도 해주는 것이 좋다
  global visited
  visited[s] = 1
  # S 노드에서 갈 수 있는 노드를 확인 후 호출
  for g in range(len(arr[s])):
    if arr[s][g] == 1:
      if visited[g] == 1: # 방문을 했다면
        continue
      dfs(g)

for tc in range(1, T+1):
  # TestCase의 첫줄에 V와 E가 주어진다.
  # V : 노드의 개수
  # E : 간선의 개수
  V, E = map(int, input().split())
  arr = [[0]*(V+1) for _ in range(V+1)]
  # E개의 줄에 걸쳐 출발 도착 노드로 간선 정보가 주어진다.
  for _ in range(E):
    x, y = map(int, input().split())
    arr[x][y] = 1 # 단방향
    # arr[x][y], arr[y][x] = 1, 1 # 양방향
  # 경로의 존재를 확인할 S와 G가 주어진다.
  # S : 출발노드
  # G : 도착노드
  S, G = map(int, input().split())

  # 방문 배열
  visited = [0] * (V + 1)

  result = 0

  dfs(S)

  if visited[G] == 1:
    result = 1

  print(f'#{tc} {result}')