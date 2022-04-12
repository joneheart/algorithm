class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):       # 노드를 추가
        new_node = Node(value)
        if self.is_empty():         # 초기에는 노드가 비어있기때문에 예외처리 필요
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):              # 데이터를 앞에서 부터 뽑는다(큐)
        if self.is_empty():
            return "비어 있습니다."
        delete_node = self.head     # 처음 헤드 값을 따로 저장한다.
        self.head = self.head.next
        return delete_node.data

    def peek(self):                 # 헤드의 값을 표시
        if self.is_empty():
            return "비어 있습니다."
        return self.head.data

    def is_empty(self):
        return self.head is None


queue = Queue()
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

print(queue.peek())
