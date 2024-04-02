import sys
sys.stdin = open('input/5174.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    stack = []
    stack.append(N)
    cnt = 1
    i = 0
    while(i < len(stack)):
        for j in range(E * 2):
            if j % 2 == 0 and arr[j] == stack[i]:
                stack.append(arr[j + 1])
                cnt += 1
        i += 1

    print(f'#{tc} {cnt}')



