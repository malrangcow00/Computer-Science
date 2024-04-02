import sys
sys.stdin = open('SWEA.input/5099.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    list1 = list(map(int, input().split()))
    queue = [i for i in range(N)]
    next_idx = N
    while len(queue) > 1:
        list1[queue[0]] //= 2
        if list1[queue[0]] == 0:
            queue.pop(0)
            if next_idx < M:
                queue.append(next_idx)
                next_idx += 1
        else:
            queue.append(queue.pop(0))
    print(f'#{tc} {queue[0]+1}')