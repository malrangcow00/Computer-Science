import sys
input = sys.stdin.readline

def print_star(N):
    if N == 1:
        return ['*']

    # recursively generate stars for N/3 size array
    unit_array = print_star(N//3)

    # initialize the new array
    new_arr = []

    # create the top part of the array
    for row in unit_array:
        new_arr.append(row * 3)

    # create the middle part of the array with empth spaces
    for row in unit_array:
        new_arr.append(row + ' ' * (N//3) + row)

    # create the bottom part of the array as reflection of the top part
    for row in unit_array:
        new_arr.append(row * 3)

    return new_arr

for row in print_star(int(input())):
    print(row)