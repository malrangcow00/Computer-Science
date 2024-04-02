for tc in range(1, 11):
    # 입력
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 로직
    total = 0
    # 열 우선 순회
    # 델타값
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]
    for i in range(N):
        for j in range(N):
            # 상하좌우 이웃한 값 순회
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                # 좌표값 확인 절차
                if 0 <= ni < N and 0 <= nj < N:
                    # (ni, nj) 좌표값과 (i, j) 좌표값의 절대값 차...
                    total += abs(arr[ni][nj] - arr[i][j])
    # 출력
    print(f"#{tc} {total}")