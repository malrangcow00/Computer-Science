# 트리 저장 방법
# 3. 인접 리스트로 저장
arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6]

# 이진 트리 만들기
nodes = [[] for i in range(14)]
for i in range(0, len(arr), 2):
    parentNode = arr[i]
    childNode = arr[i + 1]
    nodes[parentNode].append(childNode)
    # # 그래프에서 양방향일 경우
    # # 트리에서는 반대를 저장할 필요가 거의 없다
    # nodes[childNode].append(parentNode)

# 자식이 더 이상 없다는 것을 표현하기 위해 None을 삽입
for li in nodes:
    for _ in range(len(li), 2):
        li.append(None)

def preorder(nodeNumber):
    if nodeNumber == None:
        return
    print(nodeNumber, end=' ')
    preorder(nodes[nodeNumber][0])
    # print(nodeNumber, end=' ')
    preorder(nodes[nodeNumber][1])
    # print(nodeNumber, end=' ')

preorder(1)

# 이진 탐색 트리
# 삽입 연산
# 삭제 연산