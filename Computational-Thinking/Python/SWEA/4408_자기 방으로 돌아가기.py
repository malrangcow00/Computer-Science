import sys
sys.stdin = open('input/4408.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    students = []
    line = [list(map(int, input().split())) for _ in range(N)]
    cnt = [0] * 201

    for num1, num2 in line:
    #     num1 = num1 // 2 + num1 % 2
    #     num2 = num2 // 2 + num2 % 2
        num1 = (num1 + num1 % 2) // 2
        num2 = (num2 + num2 % 2) // 2
        for i in range(min(num1, num2), max(num1, num2) + 1):
            cnt[i] += 1
    print(f'#{tc} {max(cnt)}')