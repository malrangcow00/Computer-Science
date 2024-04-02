import sys
sys.stdin = open('input/5178.txt', 'r')

T = int(input())


def postorder(tree, p):
    # 기저조건... (+ 오른쪽 노드가 없는 경우도 있으므로 예외처리)
    if p > N:
        return 0
    # 가지치기...(+단말노드의 값이 있다면 그 값을 반환...)
    if tree[p] != 0:
        return tree[p]
    # 왼쪽에 있는 자식 탐색
    left = postorder(tree, p * 2)
    # 오른쪽에 있는 자식 탐색
    right = postorder(tree, p * 2 + 1)
    # 현재 노드를 탐색
    tree[p] = left + right
    return tree[p]


for tc in range(1, T + 1):
    # 입력
    # N : 노드의 수, M : 리프 노드의 수, L : 출력한 노드의 번호
    N, M, L = map(int, input().split())

    # 완전 이진 트리를 저장할 일차원 배열
    tree = [0] * (N + 1)

    for _ in range(M):
        # 노드의 번호, 노드의 값
        n, val = map(int, input().split())
        tree[n] = val

    # 로직
    # 노드값이 비어있는 노드라면 해당 값을 채워준다...
    # 후위 순회를 진행하면서 해당 노드가 비어있다면
    # (0이라면) 해당 값을 재귀함수 형태로 채워준다..
    postorder(tree, 1)

    # 출력
    # L 노드가 가지고 있는 값을 출력
    print(f"#{tc} {tree[L]}")