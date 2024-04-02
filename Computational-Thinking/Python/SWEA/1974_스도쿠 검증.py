import sys
sys.stdin = open('input/1974.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = 1
    
    # 판별자로 사용되는 1~9 배열 따로 리스트를 만들어서 여러번 쓰지 않기

    # 가로 판별
    for i in range(9):
        for j in range(9):
            if j + 1 not in arr[i]:
                result = 0
    
    # 세로 판별
    for i in range(9):
        col_list = []
        for j in range(9):
            col_list.append(arr[j][i])
        for j in range(9):
            if j+1 not in col_list:
                result = 0


    # 3*3 판별

    for i in range(3):
        for j in range(3):
            box_list = []
            for k in range(3*(i-1), 3*i):
                for l in range(3*(j-1), 3*j):
                    box_list.append(arr[k][l])
            for k in range(9):
                if k+1 not in box_list:
                    result = 0
    print(f'#{tc} {result}')

# f = open('SWEA.output/1974.txt', 'r')
# while True:
#     sol = f.readline()
#     if not sol: break
#     print(sol, end='')
# f.close()