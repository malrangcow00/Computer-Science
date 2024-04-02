import sys
sys.stdin = open('input/5176.txt', 'r')

# 중위순회 코드..
def inorder(tree, p):
    global cnt

    # 기저조건
    if p > N:
        return

    # L V R
    inorder(tree, p * 2)
    cnt += 1
    tree[p] = cnt
    inorder(tree, p * 2 + 1)


# 테스트케이스 수
T = int(input())
for tc in range(1, T + 10):
    # 입력
    # 노드의 갯수
    N = int(input())

    # 로직
    # 완전이진트리이면서,
    # 이진탐색트리에 해당되는
    # 노드 갯수가 N개인 트리를 만들어라...
    tree = [0] * (N + 1)

    # 이진탐색트리의 특징 중에 하나인
    # 중위순회를 하였을 때에 "오름차순"이
    # 된다는 특징을 사용하겠다...!
    cnt = 0  # 카운트 변수
    inorder(tree, 1)  # 중위순회를 하면서 오름차순으로 노드값을 채워넣는다..

    # 출력
    # 루트 노드와 N // 2 번째 노드의 값을 출력해라...!
    print(f"#{tc} {tree[1]} {tree[N // 2]}")