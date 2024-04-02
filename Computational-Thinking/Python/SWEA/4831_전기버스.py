T = int(input())  # 노선 개수 1 <= T <= 50
 
for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    # K: 한 번에 이동할 수 있는 정류장 수
    # N: 정류장 개수
    # M: 충전소 개수
    stations = list(map(int, input().split()))
 
    stations.append(N)  # 종점을 리스트에 추가
    pre_station = 0  # 이전 충전소
    cnt = 0  # 충전 횟수
 
    for i in range(M + 1):  # 종점이 M + 1 다음 충전소까지 참조해야하므로 i range는 M까지
        if stations[i] - pre_station > K:  
            cnt = 0  
            break
         
        if i == M or stations[i + 1] - pre_station > K:  # 다음 충전소와의 거리 체크
            if i != M:
                cnt += 1
            pre_station = stations[i]
 
    print(f'#{tc} {cnt}')