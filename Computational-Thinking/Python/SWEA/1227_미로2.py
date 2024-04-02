import sys
sys.stdin = open('input/1227.txt', 'r')

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 현재 좌표 (x, y) 좌표에서 사방탐색을 진행하여 다음 좌표로 깊게 이동한다
def dfs(arr, visited, start_x, start_y, end_x, end_y):
    # 사방탐색을 진행하여 옆의 길로 이동한다
    visited[y][x] = True
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        # 해당 좌표가 유효한지
        # 갈 수 있는 통로인지
        # 방문한적이 없는지
        if 0 <= nx < 100 and 0 <= ny <= 100 and arr[ny][nx] in [0,2,3] and visited[ny][nx] == False:
            dfs(arr, visited, nx, ny, end_x, end_y)
    # 끝점을 방문한 것이기 때문에 True를 반환
    return arr[end_y][end_x] == True

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().strip())) for i in range(100)]
    # 시작점/도착점 탐색
    for y in range(100):
        for x in range(100):
            if arr[y][x] == 2:
                start_x = x
                start_y = y
            elif arr[y][x] == 3:
                end_x = x
                end_y = y
    visited = [[False] * 100]
    dfs(arr, visited, start_x, start_y, end_x, end_y)




