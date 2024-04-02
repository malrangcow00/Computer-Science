import sys
sys.stdin = open('input/1249.txt', 'r')

# dijkstra































# # BFS, 시간/메모리 초과
# from collections import deque
# 
# # 델타 탐색을 이용해야 하기에 dx, dy를 다음과 같이 정해줌
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
# 
# def bfs(x,y):
#     q = deque()
#     q.append([x,y])
#     while q:
#         x, y = q.popleft()
#         for z in range(4):
#             nx = x + dx[z]
#             ny = y + dy[z]
#             if 0 <= nx < N and 0 <= ny < N and (my_list[nx][ny]==0 or my_list[nx][ny] > my_list[x][y] + arr[nx][ny]):
#                 # 해당 되는 지역까지 0으로 가거나, 해당되는 지역 이전까지 가는 값 + 현재 지역 값이 더 작을때
#                 my_list[nx][ny] = my_list[x][y] + arr[nx][ny] # 값을 반환해서
#                 q.append([nx,ny])
# 
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     arr = [list(map(int, input().strip())) for _ in range(N)] # 입력 값으로 나오는 보존되는 2차원 배열
#     my_list = [[0] * N for _ in range(N)] # 값 변화하는 2차원 배열
#     bfs(0,0)
#     print(f'#{tc} {my_list[N-1][N-1]}') # G에 도착할때의 값을 알아야하기에