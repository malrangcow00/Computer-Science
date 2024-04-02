import sys
sys.stdin = open('SWEA.input/4869.txt', 'r')

floor = [0] * 31

# 기저조건
floor[1] = 1
floor[2] = 3

def paper(x):
    global floor
    if x > 2:
        for i in range(3, x+1):
            floor[i] = floor[i-1] + 2 * floor[i-2]
        

        # # 뒤에서부터 재할당하면 아직 재할당되지 않은 인덱스 3이상의 0값을 불러오기 때문에 적절하지 않다.
        # if x % 2 == 0:
        #     floor[x] = floor[x-1] * 2 + 1 
        # else:
        #     floor[x] = floor[x-1] + floor[x-1] - 1
        # floor[x] = floor[x-1] + 2 * floor[x-2]

        return floor[x-1] + 2 * floor[x-2]


T = int(input())
for tc in range(1, T+1):
    # 입력
    N = int(input())//10

    # 출력
    print(f'#{tc} {paper(N)}')