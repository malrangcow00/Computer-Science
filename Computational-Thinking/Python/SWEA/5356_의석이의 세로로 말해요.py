import sys
sys.stdin = open('input/5356.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    arr = [list(input()) for _ in range(5)]
    mx_len = len(arr[0])
    for _ in arr:
        mx_len = max(mx_len, len(_))
    res = ''
    for _ in range(mx_len):
        for y in range(5):
            if _ < len(arr[y]):
                res += arr[y][_]
    print(f'#{tc} {res}')



