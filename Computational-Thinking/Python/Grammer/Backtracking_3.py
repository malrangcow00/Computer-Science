def find_subsets_with_sum(arr, total):

    # 재귀함수 형태로, 해당 depth의 원소를 부분집합에 포함하거나 하지 않는 형식
    def find_subsets(arr, N, target_sum, current_sum, bits, depth, subset):
        # 기저조건 (종료조건)
        # 부분집합의 합이 10인 경우...
        if current_sum == target_sum:
            print(subset)
            return

        # 모든 원소를 순회한 경우 종료 !
        if depth == N:
            return

        # 가지치기: 해당 원소를 더한 값이 10을 넘어가는 경우
        if current_sum > target_sum:
            return

        # 유도조건 (재귀)
        bits[depth] = True # 현재 원소를 사용하는 경우
        subset.append(arr[depth])
        find_subsets(arr, N, target_sum, current_sum + arr[depth], bits, depth+1, subset)
        subset.pop()

        bits[depth] = False # 현재 원소를 사용하지 않는 경우
        find_subsets(arr, N, target_sum, current_sum, bits, depth+1, subset)



    # 부분집항블 만들 때 필요한 임시 변수???
    # 배열의 길이
    N = len(arr)
    bits = [False] * N
    subset = []
    find_subsets(arr, N, total, 0, bits, 0, subset)

# 주어진 리스트, 합이 10인 부분집합을 출력
arr = list(range(1, 11))
total = 10
find_subsets_with_sum(arr, total)