class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        what_len = 1
        cur = self.head

        while cur.next is not None:
            cur = cur.next
            what_len +=1

        answer_len = what_len - k
        cur = self.head

        for i in range(answer_len):
            cur = cur.next

        return cur


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)
linked_list.append(9)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!





