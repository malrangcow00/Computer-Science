import random
import sys

def generate():
    sys.stdout = open("input.txt", "w+")
    T = 10
    print(T)
    for tc in range(1, T + 1):
        N = random.randint(1, 999999)
        M = random.randint(1, 10)
        print(N, M)


# 솔루션
def solution1():
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output1.txt", "w")

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

        # change 횟수 만큼 교환을 진행하고, 최댓값을 갱신한다.. DFS
        def dfs(k):
            nonlocal mx
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
        # 완전탐색 (change 횟수 만큼 교환을 진행하면서 만들 수 있는 모든 경우를 탐색..)
        dfs(0)

        # 출력
        print(f"#{tc} {mx}")


# 실패코드


def solution2():
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output2.txt", "w+")

    # 여기에 본인 코드를 넣기 (들여쓰기 맞추고 global -> nonlocal로 수정)
    def DFS(cnt, N):
        nonlocal mn
        if cnt > mn:
            return
        elif N >= distance:
            mn = min(mn, cnt)
            return
        else:
            if N + M[N] > distance-2:
                for i in range(1, distance-N+1):
                    N += i
                    cnt += 1
                    DFS(cnt, N)
                    N -= i
                    cnt -= 1
            else:
                for i in range(1, M[N]+1):
                    N += i
                    cnt += 1
                    DFS(cnt, N)
                    N -= i
                    cnt -= 1

    # T = int(input())
    # for tc in range(1, T+1):
    for tc in range(1, 2):
        arr = list(map(int, input().split()))
        N = arr[0]
        M = arr[1:]
        distance = N - 1
        mn = 99999999999999
        DFS(-1, 0)
        print(f'#{tc} {mn}')


##############################################################################

while True:
    generate()
    solution1()
    solution2()
    # output1.txt 파일과 output2.txt 파일이 다른 경우 중지
    with open("output1.txt", "r") as fp1:
        with open("output2.txt", "r") as fp2:
            if fp1.readlines()[:9] != fp2.readlines()[:9]:
                exit()