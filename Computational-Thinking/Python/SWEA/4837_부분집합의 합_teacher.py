# 부분집합의합

T = int(input())

for tc in range(1, T + 1):
    # 입력
    N, K = map(int, input().split())

    # 로직
    # N개의 요소를 가지고 있는 부분집합을 만들고,
    # 그 합이 K인 요소를 카운트를 해라..
    cnt = 0
    # 부분집합을 만드는 코드
    # 1 ~ 12까지의 숫자를 가지는 집합
    arr = [i for i in range(1, 13)]

    # 부분집합 생성하는 코드 (비트 연산)
    for i in range(1 << 12):
        total = 0 # 부분집합 요소들의 합
        length = 0 # 부분집합의 요소 갯수
        # i의 j번째 비트가 1인 경우...
        for j in range(12):
            if i & (1 << j):
                total += arr[j]
                length += 1
        if length == N and total == K:
            cnt += 1

    # 출력
    print(f"#{tc} {cnt}")