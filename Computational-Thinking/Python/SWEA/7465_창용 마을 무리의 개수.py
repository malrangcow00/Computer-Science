import sys
path = sys._getframe().f_code.co_filename.split('\\')[-1]
problem_number = ''
for _ in path:
    if _.isdigit():
        problem_number += _
sys.stdin = open(f'input/{problem_number}.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    if M == 0:
        print(f'#{tc} {N}')
        continue
    humans = set(range(1, N+1))
    s, e = map(int, input().split())
    connection = [{s, e}] + [set() for _ in range(N-1)]
    humans = humans - {s, e}
    idx = 0
    for _ in range(M-1):
        new = set(map(int, input().split()))
        humans = humans - new
        if new & connection[idx]:
            connection[idx] = connection[idx] | new
        else:
            idx += 1
            connection[idx] = new
    cnt = idx+1
    for i in range(idx):
        for j in range(i+1, idx+1):
            if connection[i] & connection[j] and connection[i] and connection[j]:
                connection[i] = connection[i] | connection[j]
                connection[j] = set()
                cnt -= 1
    cnt += len(humans)
    print(f'#{tc} {cnt}')