import sys
sys.stdin = open('input/1966.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    input()
    arr = list(map(int, input().split()))
    arr.sort()
    print(f'#{tc}', *arr)

# def bs(list, num):
#     # N번째 요소 부터 감소.
#     for k in range(num-1, 0, -1):
#         # 0번째 요소 부터 k-1번째 요소 까지 증가
#         for j in range(0, k):
#             # j번째 요소가 j번째 요소 보다 클 경우 두 요소의 위치를 변경
#             if list[j] > list[j + 1]:
#                 list[j], list[j + 1] = list[j + 1], list[j]
#         print(list)
#     # 반환
#     return list
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     ans = list(map(int, input().split()))
#     bs(ans, N)
#     print(f'#{tc}', end=' ')
#     print(*ans)