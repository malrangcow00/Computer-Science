# 전기버스
T = int(input())
for tc in range(1, T + 1):
    # 입력
    # K: 버스가 한번에 갈 수 있는 거리
    # N: 시작점과 종점 사이의 거리
    # M: 충전기가 놓여있는 댓수
    K, N, M = map(int, input().split())
    arr = [0] + list(map(int, input().split())) + [N]  # 충전기에 대한 좌표 리스트

    # 충전 횟수
    charged = 0
    # 버스의 현재 위치 (출발점부터)
    start = 0
    for i in range(1, M + 2):
        # 충전기 설치가 잘못된 경우 (충전기 사이의 거리가 K 초과인 경우)
        if arr[i] - arr[i - 1] > K:
            charged = 0
            break
        # 버스가 출발점 (현재 위치에서) 다음위치로 넘어갈 수 있는지 확인
        if arr[i] - start > K:
            start = arr[i - 1]
            charged += 1

    print(f"#{tc} {charged}")