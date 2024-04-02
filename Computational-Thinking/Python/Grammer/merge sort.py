def merge_sort(arr):
    global new_arr
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
            i += 1
        else:
            new_arr.append(right[j])
            j += 1

    while i < len(left):
        new_arr.append(left[i])
        i += 1

    while j < len(right):
        new_arr.append(right[j])
        j += 1

    return new_arr

arr = [4, 5, 1, 3, 2]

print(merge_sort(arr)) # last new_arr