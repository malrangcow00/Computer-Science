import sys
input = sys.stdin.readline


s0 = ['m', 'o', 'o']


def moo(N, pre_len, depth):  # pre_len: 이전 차수의 길이, # depth: 차수
    # 다음 길이
    new_len = 2 * pre_len + depth + 3
    if N <= 3:  # N이 3 이하일 경우 바로 출력
        print(s0[N - 1])
        return

    if new_len < N:  # new_len이 N보다 작을 경우
        moo(N, new_len, depth + 1)  # depth(차수)를 하나 늘림. new_len이 N을 담을 수 있을 때까지
    else:
        # N은 pre_len(이전 길이)보다 무조건 큼.
        # 가운데, 뒤 파트만 보면 됨
        # 가운데
        if pre_len < N and N <= pre_len + depth + 3:
            if N - pre_len != 1:  # N - pre_len = 1일때만 'm'이 있고 나머지는 'o'로 채워진다.
                print('o')
            else:
                print('m')
            return
        # 뒤
        else:  # pre_len+depth+3 바깥에 있는 경우
            # [N - (pre_len + depth + 3)]을 진행해서 다시 첫번째 파트로 돌아온 다음 처음부터 재귀를 돌리기 시작한다.
            moo(N - (pre_len + depth + 3), 3, 1)


N = int(input())
moo(N, 3, 1)