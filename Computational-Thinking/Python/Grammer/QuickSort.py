# 함수 안의 함수 (nested function : 중첩 함수)
# 내부 함수 (inner function)
# 퀵소트 함수 작성
def quick_sort(A, left, right):
    # 왼쪽 오른쪽 범위 나누어서 정렬... (pivot 중간값으로 해서 범위를 정복)
    if left < right:
        pivot_index = partition(A, left, right)
        quick_sort(A, left, pivot_index - 1)
        quick_sort(A, pivot_index + 1, right)


# 호어 partition 로직...
def partition(A, left, right):
    i = left
    j = right
    pivot = A[i]
    # 인덱스 i -> ...  <- j 서로 교차할 때까지
    while i <= j:
        while i <= j and A[i] <= pivot:
            i += 1
        while i <= j and A[j] >= pivot:
            j -= 1
        # 인덱스를 이동하고 스왑하는 과정을 진행...
        if i < j:
            # swap i <-> j
            A[i], A[j] = A[j], A[i]

    # 반복이 끝난 후에 ... 최종적으로 피봇을 중앙에 넣는다.
    # swap left <-> j
    A[left], A[j] = A[j], A[left]

    # 피봇 인덱스를 반환한다...
    return j


arr1 = [11, 45, 23, 81, 28, 34]
arr2 = [11, 45, 22, 81, 23, 34, 99, 22, 17, 8]
arr3 = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

quick_sort(arr1, 0, len(arr1) - 1)
quick_sort(arr2, 0, len(arr2) - 1)
quick_sort(arr3, 0, len(arr3) - 1)

print(arr1)
print(arr2)
print(arr3)

# # 퀵 정렬은 추가적인 메모리를 사용하지 않기 때문에 아래 함수는 병합정렬에 가깝다.
# def QuickSort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[0]
#     left = []
#     right = []
#     for i in range(1, len(arr)):
#         if arr[i] < pivot:
#             left.append(arr[i])
#         else:
#             right.append(arr[i])
#     return QuickSort(left) + [pivot] + QuickSort(right)
