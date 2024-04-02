# line 일차원 배열에 활주로를 설치할 수 있다면 True, (없다면 False)
def check(line, X):
    cnt = [0] * len(line)  # 경사로를 설치한 갯수 카운팅 배열
    for i in range(len(line) - 1):
        # 비탈길이 있는 영역을 먼저 찾는다
        # 2 -> 3
        if line[i] == line[i + 1] - 1:  # 비탈길이 올라가는 경우
            if 0 <= i - 1 and line[i - 1] == max(line[i-X+1:i+1]) == min(line[i-X+1:i+1]) :  # 비탈길을 설치하면 되는 상황...
                # 경사로를 설치해준다...
                for j in range(i, i - X, -1):
                    cnt[j] += 1
            else:  # 경사로를 설치할 수 없는 상황
                return False
        # 3 -> 2
        elif line[i] == line[i + 1] + 1:  # 비탈길이 내려가는 경우
            if i + 2 < N and line[i + 1] == line[i + 2]:  # 경사로를 설치할 수 있음.. <- 이 부분도 수정이 필요함!
                for j in range(i + 1, i + X + 1):
                    cnt[j] += 1
            else:  # 경사로를 설치할 수 없는 상황
                return False
        # 3 -> 3
        elif line[i] == line[i + 1]:  # 평지로 그대로 이동할 때
            pass
        # 2 -> 4이상, 4 -> 2이하 , 경사로를 설치하지 못할 때
        else:
            return False

    # 경사로 설치 갯수를 보면서 겹쳐 있으면 활주로가 불가능한 상태...
    if max(cnt) == 2:
        return False

    return True

T = int(input())
for tc in range(1, T + 1):
    N, X = map(int, input().split())
    graph = [list(map(int, input().split())) for i in range(N)]

    # 카운트 변수
    cnt = 0
    # 전치 행렬 (행 <-> 열)
    graph_t = [list(i) for i in list(zip(*graph))]

    for i in range(N):
        # 해당되는 가로줄에 활주로를 건설할 수 있는가?
        if check(graph[i], X):
            cnt += 1

    for i in range(N):
        # 해당되는 세로줄에 활주로를 건설할 수 있는가?
        if check(graph_t[i]):
            cnt += 1