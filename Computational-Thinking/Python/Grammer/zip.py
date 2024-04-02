arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print('원본 2차원 배열')
for _ in range(len(arr)):
    print(''.join(map(str, arr[_])))
print()

# 전치행렬
arr_e = list(zip(*arr))

# 90도 회전
arr_1 = list(zip(*arr[::-1]))

# 180도 회전
arr_2 = list(zip(*arr_1[::-1]))

# 270도 회전
arr_3 = list(zip(*arr_2[::-1]))

print('전치행렬: 행과 열 변환')
for _ in range(len(arr_e)):
    print(''.join(map(str, arr_e[_])))
print()

print('90도 회전')
for _ in range(len(arr_1)):
    print(''.join(map(str, arr_1[_])))
print()

print('180도 회전')
for _ in range(len(arr_2)):
    print(''.join(map(str, arr_2[_])))
print()

print('270도 회전')
for _ in range(len(arr_3)):
    print(''.join(map(str, arr_3[_])))