import sys
input = sys.stdin.readline

def merge_sort(arr):
    # 길이가 1일 경우 그대로 나열
    if len(arr) == 1:
        return arr
    
    # 배열을 나눌 중간점 설정 후 길이가 1이 될 때까지 나눈다
    mid = (len(arr) + 1) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    new_arr = []
    i = 0
    j = 0

    # 나뉜 배열을 인덱스 비교하며 정렬
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new_arr.append(left[i])
            sorted_arr.append(left[i])
            i += 1
        else:
            new_arr.append(right[j])
            sorted_arr.append(right[j])
            j += 1

    while i < len(left):
        new_arr.append(left[i])
        sorted_arr.append(left[i])
        i += 1

    while j < len(right):
        new_arr.append(right[j])
        sorted_arr.append(right[j])
        j += 1

    return new_arr

N, K = map(int, input().split())
arr = list(map(int, input().split()))

sorted_arr = []
merge_sort(arr)

if len(sorted_arr) >= K:
    print(sorted_arr[K-1])
else:
    print(-1)