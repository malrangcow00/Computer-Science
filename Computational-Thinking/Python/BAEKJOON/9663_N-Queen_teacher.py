import sys
input = sys.stdin.readline

def check(x):
    # i: 행 row[n]: 열
    for i in range(x):
        # 열(row[n])이 같거나 같은 대각선상에 위치하면(x좌표 차이와 y좌표 차이가 같을 경우) False
        if row[x] == row[i] or x - i == abs(row[x] - row[i]):
            return False
    return True

def dfs(x):
    global cnt
    if x == N:
        cnt += 1
    else:
        # 열 번호 i(0부터 N-1까지)에 퀸을 두면서 탐색
        for i in range(N):
            row[x] = i
            if check(x): # 체크 결과 True이면 백트래킹 없이 진행
                dfs(x + 1)

N = int(input())
row = [0] * N
cnt = 0
dfs(0)
print(cnt)
