import sys
sys.stdin = open('input/4864.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    str_1 = input()
    str_2 = input()
    res = 0
    if str_1 in str_2:
        res = 1
    print(f'#{tc} {res}')
