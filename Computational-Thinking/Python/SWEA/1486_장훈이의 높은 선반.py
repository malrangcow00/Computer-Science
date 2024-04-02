import sys, os, re
path = os.path.basename(__file__)
problem_number = re.compile('^([0-9]{4,})').match(path).group(1)
sys.stdin = open(f'input/{problem_number}.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    # N: 점원의 수 B: 선반의 높이
    N, B = map(int, input().split())
    # 점원들의 키의 배열 입력
    heights = list(map(int, input().split()))
    # 최소값 초기설정
    min_height = sum(heights)
    # 비트 연산으로 조합 생성
    for i in range(1 << N):
        # 인간탑의 높이
        height = 0
        for j in range(N):
            if i & (1 << j):
                height += heights[j]
        # 최소값 갱신
        if height >= B and height < min_height:
            min_height = height
    # 선반에 닿는 인간탑의 최소 높이와 선반 높이의 차이를 출력
    print(f'#{tc} {min_height-B}')