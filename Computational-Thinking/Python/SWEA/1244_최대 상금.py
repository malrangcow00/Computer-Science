import sys
sys.stdin = open('input/1244.txt', 'r')

T = int(input())
def shuffle(num, depth):
    global mx
    if depth == cnt:
        mx = max(mx, int(''.join(num)))
    else:
        for i in range(len(num)-1):
            for j in range(i+1, len(num)):
                num[i], num[j] = num[j], num[i]
                shuffle(num, depth + 1)
                num[i], num[j] = num[j], num[i]
for tc in range(1, T+1):
    num, cnt = map(str, input().split())
    num = list(num)
    cnt = int(cnt)
    mx = 0
    shuffle(num, 0)
    print(f'#{tc} {mx}')