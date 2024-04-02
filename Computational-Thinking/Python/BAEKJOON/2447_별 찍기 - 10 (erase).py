import sys
input = sys.stdin.readline

def erase_star(arr):
    N = len(arr)
    if N == 1:
        return '*'
    part_1 = erase_star([arr[_][:N//3] for _ in range(N//3)])
    part_2 = erase_star([arr[_][N//3:2*N//3] for _ in range(N//3)])
    part_3 = erase_star([arr[_][2*N//3:] for _ in range(N//3)])

    part_4 = erase_star([arr[_][:N//3] for _ in range(N//3, 2*N//3)])
    # 빈 배열
    part_5 = [' '*(N//3) for _ in range(N//3)]
    part_6 = erase_star([arr[_][2*N//3:] for _ in range(N//3, 2*N//3)])

    part_7 = erase_star([arr[_][:N//3] for _ in range(2*N//3, 3*N//3)])
    part_8 = erase_star([arr[_][N//3:2*N//3] for _ in range(2*N//3, 3*N//3)])
    part_9 = erase_star([arr[_][2*N//3:] for _ in range(2*N//3, 3*N//3)])

    new_arr = []
    tmp = []

    tmp.append(part_1)
    tmp.append(part_2)
    tmp.append(part_3)

    new_arr.append(tmp)
    tmp.clear()

    tmp.append(part_4)
    tmp.append(part_5)
    tmp.append(part_6)

    new_arr.append(tmp)
    tmp.clear()

    tmp.append(part_7)
    tmp.append(part_8)
    tmp.append(part_9)

    new_arr.append(tmp)
    tmp.clear()

# 모든 배열을 다시 합
    return new_arr

N = int(input())
# create default array
arr = ['*' * N for _ in range(N)]
for row in erase_star(arr):
    print(row)