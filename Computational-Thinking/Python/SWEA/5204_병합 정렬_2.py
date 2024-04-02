import sys
sys.stdin = open('input/5204.txt', 'r')

def merge_sort(arr):
    global cnt
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    if left[-1] > right[-1]:
        cnt += 1

    tmp = left + right
    tmp.sort()
    return tmp

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    print(f'#{tc}', merge_sort(arr)[N//2], cnt)