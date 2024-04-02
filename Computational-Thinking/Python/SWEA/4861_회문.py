import sys
sys.stdin = open('input/4861.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    # M자의 단어를 받아올 때는 리스트 내의 항목 순회
    found = False
    for y in range(N):
        if found == True:
            break
        for _ in range(N-M+1):
            if arr[y][_:M+_] == arr[y][_:M+_][::-1]:
                print(f'#{tc}', ''.join(arr[y][_:M+_]))
                found = True
                break

    # 전치 행렬로 변환
    arr = list(zip(*arr))
    # for y in range(N):
    #     for x in range(N):
    #         if x < y:
    #             arr[x][y], arr[y][x] = arr[y][x], arr[x][y]
    # 기존행렬에 전치행렬을 extend 해준 뒤 횡 탐색을 한번만 시행하는 것도 효과적

    # 동일 과정 반복
    for y in range(N):
        if found == True:
            break
        for _ in range(N-M+1):
            if arr[y][_:M+_] == arr[y][_:M+_][::-1]:
                print(f'#{tc}', ''.join(arr[y][_:M+_]))
                found = True
                break