# 선형큐
# 정적인 크기의 배열
QSIZE = 100
queue = [0] * 100

# 머리, 꼬리 해당되는 인덱스 초기화
front = rear = -1


# 큐 삽입 연산 enQueue
# rear, 꼬리를 1 증가,
# 해당 위치 요소를 삽입
def enQueue(item):
    global rear
    rear = rear + 1
    queue[rear] = item


# 큐 삭제 연산 deQueue
# front, 머리를 1 증가,
# 해당 위치 요소를 삭제
def deQueue():
    global front
    front = front + 1
    return queue[front]


# 부가 연산을 만들어줘야 한다..
# 큐가 차있는지...
def isFull():
    return rear == QSIZE - 1


# 큐가 비어있는지...
def isEmpty():
    return front == rear


# 큐에 뽑을 원소의 값은 무엇인지..
def qPeek():
    return queue[front + 1]