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
        # 구현해보세요!

        cur = self.head
        answer = self.head
        length = 0
        while cur.next is not None:
            length += 1
            cur = cur.next
        index = length + 1 - k
        for i in range(index):
            answer = answer.next
        return answer


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)


print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!