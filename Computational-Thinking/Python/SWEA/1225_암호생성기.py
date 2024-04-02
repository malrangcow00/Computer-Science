import sys
sys.stdin = open('input/1225.txt', 'r')

for _ in range(10):
    tc = int(input())
    arr = list(map(int, input().split()))
    i = 1
    while True:
        n = arr.pop(0)
        arr.append(n - i)
        if arr[-1] <= 0:
            arr[-1] = 0
            break
        i += 1
        if i == 6:
            i -= 5
    print(f'#{tc} ', *arr)