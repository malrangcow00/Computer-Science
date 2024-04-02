import sys
sys.stdin = open('input/1289.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    # target: 원래의 메모리 값 (이진수)
    target = input()
    # bi: 초기화 상태 (이진수)
    bi = '0' * len(target)
    # cnt: 메모리를 덮어씌우는 횟수
    cnt = 0
    while bi != target:
        # N, M: 덮어씌운 후의 새로운 길이 입력
        N, M = len(bi), len(target)
        # 변환 과정에서 이진수 앞자리 0이 제거 되어
        # 원래 상태보다 길이가 더 짧아진 경우, 길이 차이만큼 앞에 0을 추가
        if N < M:
            bi = '0'*(M-N) + bi
        # 첫 자리수가 같을 경우 그 다음 자리부터 크기를 비교
        elif bi[0] == target[0]:
            bi, target = bi[1:], target[1:]
        # 길이가 같고 앞자리가 다른 경우 비트연산을 통해 해당자리부터 모든 뒷자리를 변경해서 덮어씌운다
        else:
            # 모든 자리수에 해당하는 1값을 통해 비트연산을 진행하여 값을 덮어우고 카운트 + 1
            bi = format(int(bi, 2)^(2**N-1), 'b')
            cnt += 1
    print(f'#{tc} {cnt}')

# T = int(input())
# for tc in range(1, T+1):
#     target = list(map(int, input()))
#     i = 1
#     cnt = 0
#     for _ in target:
#         if _ == i:
#             i = (i + 1) % 2
#             cnt += 1
#     print(f'#{tc} {cnt}')