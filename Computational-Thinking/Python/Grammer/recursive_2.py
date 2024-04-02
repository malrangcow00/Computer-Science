def recur(depth, N, nums, used):
    """
    :param depth: 재귀호출을 몇번 진행했는지 (카운트값)
    :param nums: 1~3 까지의 원소를 담는 리스트
    :return: 없음
    """
    # 기저조건 (종료조건)
    if depth == N+1:
        # 요소의 값을 출력한다...
        # for i in nums:
        #     print(i, end='-')
        print("-".join([str(num) for num in nums]))
        return
    # 유도조건 (재귀호출)
    # i : 1 -> 3
    for i in range(1, N+1):
        if used[i] == False:  # 사용했는지 여부 체크
            nums.append(i)  # 결정
            used[i] = True  # 사용했음을 체크
            recur(depth + 1, N, nums, used)
            nums.pop()  # 복구
            used[i] = False  # 복구

N = 3
used = [False] * (N + 1)
nums = []
recur(1, N, nums, used)