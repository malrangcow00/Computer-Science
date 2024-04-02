T = int(input())
A = [_ for _ in range(1, 13)]
for tc in range(1, T+1):
    # 1부터 12까지의 숫자를 원소로 가진 집합 A에서
    # 부분 집합 중 N개의 원소를 갖고 원소의 합이 K인 부분집합의 개수를 구하시오.
    N, K = map(int, input().split())
    # 원소가 12개인 모집합 A의 부분집합의 개수
    total_subsets = 2 ** 12
    # 조건을 만족하는 부분집합의 수
    cnt = 0
    for i in range(total_subsets):
        tmp_lst = []
        # 이진법 각자리를 의미하는 2 ** j (0~12범위)를 나눈 몫을 
        # 반복문으로 확인해 해당 위치 원소 유무를 판별
        # 동일한 경우 부분집합으로서 리스트로 추가
        for j in range(12):
            if i // (2 ** j) % 2 == 1:
                tmp_lst.append(A[j])
        # 조건을 만족하는 부분집합을 카운트
        if len(tmp_lst) == N and sum(tmp_lst) == K:
            cnt += 1
    # 출력
    print(f'#{tc} {cnt}')

# --------------------------------------------------------------

# arr = [_ for _ in range(1, 13)]

# N = len(arr)  # N : 원소의 개수 (배열의 길이)

# for subset in range(1 << N):  # 1 << N : 부분 집합의 개수

#     tmp_lst = []

#     for i in range(N):  # 각 자리수(원소의 개수만큼) 비트를 비교
#         if subset & (1 << i):  # subset의 i번 비트에 원소가 존재(1)하는 경우
#             tmp_lst.append(arr[i])  # 인덱스 i의 원소를 해당 부분집합에 추가

#     # # 출력 조건
#     # if len(tmp_lst) == N or sum(tmp_lst) == K:
#     #     print(tmp_lst)

#     print(tmp_lst)