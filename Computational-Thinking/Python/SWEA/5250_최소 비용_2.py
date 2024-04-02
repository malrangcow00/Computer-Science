import sys
sys.stdin = open('input/5250.txt')
import heapq

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dijkstra():
    arr[0][0] = 0  # 연료소비량
    min_heap = [(0, 0, 0)]

    while min_heap:
        cur_v, x, y = heapq.heappop(min_heap)  # 현재 연료소비량, x, y 좌표
        # 지금까지의 최소값이 현재 연료소비량 보다 작으면 continue
        if cur_v > arr[x][y]:
            continue
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if nx in range(0, N) and ny in range(0, N):
                cnt = 1  # 한칸 이동
                if box[nx][ny] > box[x][y]:
                    cnt += box[nx][ny] - box[x][y]  # 높이 차 더해주기
                new_v = cur_v + cnt  # new_v -> 현재 연료소비량 + 이동 + 높이 차
                if arr[nx][ny] > new_v:   # 최소값(연료소비량) 갱신
                    arr[nx][ny] = new_v
                    heapq.heappush(min_heap, (new_v, nx, ny))

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 가로, 세로 칸수
    box = [list(map(int, input().split())) for _ in range(N)]
    arr = [[10000000]*N for _ in range(N)]  # 연료소비량 저장
    dijkstra()
    print(f'#{tc} {arr[N-1][N-1]}')