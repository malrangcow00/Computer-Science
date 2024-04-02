# nPk : n개의 값에서 k를 선택해 뽑으세요. 순열 (재귀)
def P(arr, n, k, depth):
    # 기저조건
    if depth == k:
        # 만들어진 순열을 출력한다...
        # for i in range(k):
        #     print(arr[i], end=' ')
        # print()
        print(arr[:k])
        return

    # 유도조건
    s = depth
    for e in range(s, n):
        # s <-> e 스왑 (결정)
        arr[s], arr[e] = arr[e], arr[s]
        # 재귀호출
        P(arr, n, k, depth + 1)
        # s <-> e 스왑 (복구)
        arr[s], arr[e] = arr[e], arr[s]


arr = [1, 3, 5, 7, 9, 10]
N = 6  # len(arr)

P(arr, N, 3, 0)  # 6P3 경우의 수를 모두 출력해봐라...