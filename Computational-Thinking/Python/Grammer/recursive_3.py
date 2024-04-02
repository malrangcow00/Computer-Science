# nPk : n개의 값에서 k를 선택해 뽑으세요. 순열 (재귀)
def P(arr, n, k, used, picks, depth):
    """
    :param arr: 뽑고자 하는 배열 (요소의 갯수는 n개)
    :param n: 배열의 길이
    :param k: 뽑고자 하는 요소의 갯수
    :return: 없음
    """
    # 기저조건
    if depth == k:  # K 만큼 뽑았다면 정지..
        # 내가 지금까지 뽑은 값을 출력
        print(picks)
        return
    # 유도조건 (재귀)
    # 모든 배열 요소값에 대해서 순회 (인덱스 순회)
    for i in range(n):
        # 사용여부
        if used[i] == False:  # 사용하지 않은 수라면..
            # 결정 : 사용(사용을 했다 체크)
            used[i] = True
            picks.append(arr[i])  # 해당 숫자를 픽에 추가.
            P(arr, n, k, used, picks, depth + 1)  # 재귀 호출
            # 복구
            used[i] = False
            picks.pop()


arr = [1, 3, 5, 7, 9, 10]
N = 6  # len(arr)
used = [False] * (N)  # 사용한 값을 표기
picks = []  # 내가 뽑을 k개의 값을 담을 리스트

P(arr, N, 3, used, picks, 0)  # 6P3 경우의 수를 모두 출력해봐라...