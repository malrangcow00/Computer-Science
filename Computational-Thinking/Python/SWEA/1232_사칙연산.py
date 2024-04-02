import sys
sys.stdin = open('input/1232.txt', 'r')


def postorder(node):

    if left[node]:
        # 왼쪽 자식 노드가 있다면 왼쪽 노드를 탐색
        op_1 = postorder(left[node])

    if right[node]:
        # 오른쪽 자식 노드가 있다면 오른쪽 노드 탐색
        op_2 = postorder(right[node])

        if tree[node] in '+-*/':
            if tree[node] == '+':
                tree[node] = op_1 + op_2
            elif tree[node] == '-':
                tree[node] = op_1 - op_2
            elif tree[node] == '*':
                tree[node] = op_1 * op_2
            else:   # tree[node] == '/':
                tree[node] = op_1 // op_2

    return tree[node]

'''
[0, 1, 2, 3, 4, 5, 6]
[0, '-', '-', 10, 88, 65]
[0, 2, 4, 0, 0, 0]
[0, 3, 5, 0, 0, 0]

[0, 13, 23, 10 88, 65 ]
'''
# LRV
# 1 번 부터 시작 -> 왼쪽자식 탐색, 오른쪽 자식 탐색


# - - - - - - - - - - - - - - - - - - - - - - - - - -

for test_case in range(1, 10+1):
    # 입력
    N = int(input())
    tree = [0]*(N+1)    # 노드 value를 담을 tree
    left = [0]*(N+1)    # 노드의 왼쪽 자식 정보
    right = [0]*(N+1)   # 노드의 오른쪽 자식 정보


    answer = 0

    for _ in range(N):
        # 자식을 가지고 있는 노드 or 리프 노드
        node_info = list(input().split())
        if node_info[1].isdigit():
            tree[int(node_info[0])] = int(node_info[1])
        else:
            tree[int(node_info[0])] = node_info[1]
            left[int(node_info[0])] = int(node_info[2])
            right[int(node_info[0])] = int(node_info[3])

    '''
    [0, '-', '-', 10, 88, 65]
    [0, 2, 4, 0, 0, 0]
    [0, 3, 5, 0, 0, 0]
    '''

    answer = postorder(1)

    # [0, 13, 23, 10, 88, 65]

    print(f'#{test_case} {answer}')