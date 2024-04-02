import sys
sys.stdin = open('input/1961.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # # 행과 열 변환
    # arr_test = list(zip(*arr))
    arr_1 = list(zip(*arr[::-1]))
    arr_2 = list(zip(*arr_1[::-1]))
    arr_3 = list(zip(*arr_2[::-1]))
    print(f'#{tc}')
    for i in range(len(arr)):
        print(''.join(map(str, arr_1[i])), end=' ')
        print(''.join(map(str, arr_2[i])), end=' ')
        print(''.join(map(str, arr_3[i])))