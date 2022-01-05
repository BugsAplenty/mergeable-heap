from SinglyLinkedList import SinglyLinkedList
from Node import Node


class SinglyLinkedListSorted(SinglyLinkedList):
    def __init__(self):
        super().__init__()

    def insert(self, data):
        node_new = Node(data)
        if self.head is None:
            self.head = node_new
        elif self.head.data >= node_new.data:
            node_new.next = self.head
            self.head = node_new
        else:
            current = self.head
            while current.next and node_new.data > current.next.data:
                current = current.next
            node_new.next = current.next
            current.next = node_new

    def merge(self, other):
        if not (isinstance(other, type(self))):
            raise TypeError(f"This operation can only be performed with an object of type {type(self).__name__}.")
        dummy_node = Node(0)
        tail = dummy_node
        current = self.head
        while True:
            if current.head is None:
                return other
                break
            if current.head is None:
                return current
                break
            if current.head.data <= other.head.data:
                tail.next = current.head
                current.head = current.head.next
            else:
                tail.next = other.head
                other.head = other.head.next
            tail = tail.next
        return dummy_node.next

    def delete(self, key):
        super().delete(key)

