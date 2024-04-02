import sys
sys.stdin = open('SWEA.input/5099.txt', 'r')

from queue import deque
T = int(input())

for tc in range(1, T+1):
    # N : 화덕의 크기
    # M : 피자의 개수
    N, M = map(int, input().split())
    # Ci : 피자에 뿌려진 치즈의 양
    Ci = deque(map(int, input().split()))
    # 화덕에 들어간 피자
    stack = []
    # 현재 화덕에 들어있는 피자의 번호
    posit = [0] * N
    # 현재 피자 번호
    position_cnt = 1
    finish = False
    while True:
        if finish == True:
            break
        elif len(stack) < N:
            tmp = Ci.popleft()
            posit[len(stack)] = position_cnt
            stack.append(tmp)
            position_cnt += 1
        else:
            for _ in range(N):
                if sum(stack) == 1 and Ci == deque():
                    idx = N - stack[::-1].index(1) - 1
                    print(f'#{tc} {posit[idx]}')
                    finish = True
                    break
                if stack[_] != 0:
                    stack[_] = stack[_]//2
                if stack[_] == 0 and Ci != deque():
                    stack.pop(_)
                    tmp = Ci.popleft()
                    stack.insert(_, tmp)
                    posit[_] = position_cnt
                    position_cnt += 1