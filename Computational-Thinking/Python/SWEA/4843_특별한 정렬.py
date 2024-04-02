import sys
sys.stdin = open('input/4843.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    input()
    arr = list(map(int, input().split()))
    result = []
    i = 0
    while arr:
        if i == 10:
            break
        elif i % 2 == 0:
            result.append(max(arr))
            arr.pop(arr.index(max(arr)))
        else:
            result.append(min(arr))
            arr.pop(arr.index(min(arr)))
        i += 1
    print(f'#{tc}', *result)
