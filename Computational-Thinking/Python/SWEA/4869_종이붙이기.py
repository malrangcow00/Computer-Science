import sys
sys.stdin = open('input/4869.txt', 'r')

floor = [0] * 31

# 기저조건
floor[1] = 1
floor[2] = 3

# x % 2 == 0
# floor[x] = floor[x-1] * 2 + 1 
# x % 2 == 1
# floor[x] = floor[x-1] + floor[x-1] - 1

# floor[x-1] = floor[x-2] * 2 + 1
# 두번째 floor[x-1]에 대입하면 점화식 완성

# floor(x) = floor(x-1) + 2 * floor(x-2)

for x in range(3, 31):
    floor[x] = floor[x-1] + 2 * floor[x-2]

T = int(input())
for tc in range(1, T+1):
    # 입력
    N = int(input())//10

    # 출력
    print(f'#{tc} {floor[N]}')