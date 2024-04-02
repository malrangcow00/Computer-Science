import sys
sys.stdin = open('input/2105.txt', 'r')

T = int(input())

def dfs(y,x,path,way):
    global cnt, i, j

    if way == 3 and y == i and x == j and len(path)>=4:
        cnt = max(cnt,len(path))
        return

    elif 0 <= x < N and 0<= y < N and mapp[y][x] not in path:
        new_path = path +[mapp[y][x]]
        ny = y+my[way]
        nx = x+mx[way]
        dfs(ny,nx,new_path,way)
        if way < 3:
            ny = y+my[way+1]
            nx = x+mx[way+1]
            dfs(ny,nx,new_path,way+1)
    else:
        return


for testcase in range(1,T+1):
    N = int(input())
    mapp = [list(map(int,input().split())) for _ in range(N)]
    cnt = -1
    mx = [1,-1,-1,1]
    my = [-1,-1,1,1]
    for i in range(N):
        for j in range(N):
            dfs(i,j,[],0)

    print(f"#{testcase} {cnt}")