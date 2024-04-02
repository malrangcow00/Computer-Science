arr = [_ for _ in range(1, 6)]

N = len(arr)  # N : 원소의 개수 (배열의 길이)

for subset in range(1 << N):  # 1 << N : 부분 집합의 개수

    tmp_lst = []

    for i in range(N):  # 각 자리수(원소의 개수만큼) 비트를 비교
        if subset & (1 << i):  # subset의 i번 비트에 원소가 존재(1)하는 경우
            tmp_lst.append(arr[i])  # 인덱스 i의 원소를 해당 부분집합에 추가

    # # 출력 조건
    # if len(tmp_lst) == N or sum(tmp_lst) == K:
    #     print(tmp_lst)
    print(tmp_lst)