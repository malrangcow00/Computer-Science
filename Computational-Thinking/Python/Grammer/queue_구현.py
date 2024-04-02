class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class queue:
    def __init__(self):
        self.size = 0
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.size == 0

    def enqueue(self, data):
        if self.is_empty():
            self.rear = node(data)
            self.front = self.rear
        else:
            self.rear.next = node(data)
            self.rear = self.rear.next
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print('Queue_Empty')
        elif self.size == 1:
            res = self.front.data
            self.front = None
            self.rear = None
            self.size -= 1
            return res
        else:
            res = self.front.data
            self.front = self.front.next
            self.size -= 1
            return res

    def Qpeek(self):
        if self.is_empty():
            print('Queue_Empty')
        else:
            return self.front.data


q = queue()
for i in range(1, 4):
    q.enqueue(i)
for i in range(3):
    print(q.Qpeek())
    print(q.dequeue())