import sys
sys.stdin = open('input/1954.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    # 델타 : 우하좌상 (2차원 배열 내 y 좌표 부호 주의)
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # 출발 좌표
    x, y = 0, 0

    # 방향값
    direction = 0
    cnt = 1 # 카운트
    arr[0][0] = 1
    while cnt < N * N:
        # 델타값 순서대로 쭈우욱 진행을 하다가
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 정상적으로 카운트 값을 넣어야 하는 경우라면
        if 0 <= nx < N and 0 <= ny < N and arr[ny][nx] == 0:
            x, y = nx, ny
            cnt += 1
            arr[ny][nx] = cnt
        # 벽을 만나거나, 기존에 값이 있었던 지역을 만나면
        else:
            # 다음 델타값으로 변경 (턴 진행)
            direction = (direction + 1) % 4
    print(f'#{tc}')
    for row in arr:
        print(*row)