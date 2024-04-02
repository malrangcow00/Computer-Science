import sys
sys.stdin = open('input/1244.txt', 'r')

# change 횟수 만큼 교환을 진행하고, 최댓값을 갱신한다.. DFS
def dfs(k):
    global mx
    val = int(''.join(nums))  # 123

    # 기존에 진행했던 순회라면 진행하지 않도록 종료!
    if val in visited[k]:
        return
    # 금액, 재귀호출횟수를 기록
    visited[k].add(val)

    # 기저조건 (change 횟수 만큼 교환...)
    if k == change:
        # 최댓값을 갱신...
        # ['1', '2', '3']

        if val > mx:
            mx = val  # 최댓값 갱신
        return

    # i : 바꿀 번호판의 앞쪽 숫자
    # j : 바꿀 번호판의 뒷쪽 숫자
    for i in range(length - 1):  # (N - 1 까지 진행하면 최소 뒤에 1개를 남길 수 없으므로.. - 1)
        for j in range(i + 1, length):  # (i + 1 인 이유는 앞에 최소 1개는 남아있어야 하므로..)
            # i <-> j 번호판을 교환...
            nums[i], nums[j] = nums[j], nums[i]  # 결정
            dfs(k + 1)
            nums[i], nums[j] = nums[j], nums[i]  # 복구


T = int(input())
for tc in range(1, T + 1):
    # 입력
    # 숫자판의 정보, 교환횟수
    nums, change = input().split()  # "123", "1"
    # 숫자판의 정보는 리스트로 형변환
    nums = list(nums)  # ['1', '2', '3']
    # 교환 횟수는 정수 형변환
    change = int(change)

    length = len(nums)

    # 순회별로 따로 set 자료형을 만들어서 관리...
    # visited = set()  # 순회 과정에서 중복으로 발행하는 순회 제거용... (중복체크)
    visited = [set() for _ in range(change + 1)]

    # 로직
    # 가장 큰 수 (최댓값)을 저장해서 출력...
    mx = -1
    # 완전탐색 (change 횟수 만큼 교환을 진행하면서 만들 수 있는 모든 경우를 탐색..)
    dfs(0)

    # 출력
    print(f"#{tc} {mx}")