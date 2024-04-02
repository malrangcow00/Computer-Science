import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    checks = list(input().strip())
    cnt = 0
    score = 0
    for i in checks:
        if i == 'O':
            cnt += 1
            score += cnt
        else:
            cnt = 0
    print(score)