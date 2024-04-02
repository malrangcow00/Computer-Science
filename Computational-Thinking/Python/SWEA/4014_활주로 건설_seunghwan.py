import sys
sys.stdin = open('input/4014.txt', 'r')

# 활주로는 높이가 동일한 구간에서 건설이 가능하다.
# 높이 차는 1이하일 경우에만 가능하다.
# 경사로는 범위를 벗어날 때까지 연결이 되어야 한다.
# 한 행, 한 열이 부드럽게 이어져야 한다.
def check(res):
    global ans
    cnt = 1  # 높이가 같을때 올라가는 경사로를 만들 수 있는지 체크하는 변수
    can = 1  # 한 줄이 경사로를 건설할 수 있는지 확인.
    chk = 0  # 내려가는 경사로를 건설해야 하는지 확인하는 변수
    for k in range(N):
        # 같은 범위가 x를 만족했을 때(현 위치에 경사로를 설치할 수 있을 때) 절댓값의 차가 1이면 경사로를 생성한다.
        if chk == 1:  # 내려가는 경사로를 건설해야 할 때
            if cnt == X:  # 내려가는 경사로 건설이 가능해 진다면
                can = 1  # 경사로를 건설했기 때문에 다시 초기화 한다
                cnt = 0
                chk = 0  # 건설했다고 변환
            elif k + 1 < N and res[k] == res[k + 1]:  # 범위내에서 다음 값과 높이가 같을 때
                cnt += 1  # 건설 가능한 거리 ++
                continue
            else:  # 내려가는 경사로를 건설해야 하는데 거리만큼 못채우거나
                can = 0
                break
        if k+1 < N and res[k] == res[k+1]:  # 범위내에서 다음 값과 높이가 같을 때
            cnt += 1
            continue
        elif k+1 < N and res[k] != res[k+1]:  # 범위내에서 다음 값과 높이가 다를 때, 경사로를 설치해야 할 때
            if res[k] - res[k+1] == -1 and cnt >= X:  # 올라가는 경사로 일 때 현재 높이의 길이가 X 이상이라 경사로 건설 가능
                cnt = 1
                continue
            elif res[k] - res[k+1] == 1:  # 만약 내려가는 경사로가 필요하다면
                cnt = 1
                chk = 1  # 내려가는 경사로가 필요하다고 표시
            else:  # 지형 높이차가 +- 1이 아닌 경우 건설이 불가능하다.
                can = 0  # 건설이 불가능해짐을 의미
                break
    if can == 1:
        ans += 1



T = int(input())
for tc in range(1, T+1):
    N, X = map(int, input().split())
    # 길이 X는 2이상 4이하의 정수
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0  # 지을 수 있는 경사로 만들기
    # 가로 확인을 한다.
    # 경사로가 지어진다면 경사로가 지어진 곳의 값을 바꾸어 준다.
    # 높이 차가 1이하 이면 경사로가 이어지는지 확인한다.
    # 한 행, 한 열이 전부 만족해야 한다.
    for i in range(N):
        res = []
        for j in range(N):
            res.append(arr[i][j])
        check(res)  # 한 행을 끝냈을 때 경사로가 지어질 수 있는지 확인하자.
        #print(ans)
    # 세로 확인을 한다.
    for j in range(N):
        res = []
        for i in range(N):
            res.append(arr[i][j])
        check(res)
        #print(ans)
    print(f'#{tc} {ans}')