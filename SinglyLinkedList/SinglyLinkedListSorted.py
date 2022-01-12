from SinglyLinkedList import SinglyLinkedList
from Node import Node


class SinglyLinkedListSorted(SinglyLinkedList):
    def __init__(self):
        super().__init__()

    def insert(self, data: int):
        """
        Inserts new node into sorted singly-linked list.
        :param data:
        :return:
        """
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
        """
        Merges self with other sorted singly-linked list.
        :param other:
        :return:
        """
        if not (isinstance(other, type(self))):
            raise TypeError(f"This operation can only be performed with an object of type {type(self).__name__}.")
        merge_head = temp = Node(0)
        temp_this = self.head
        temp_other = other.head
        while temp_this or temp_other:
            if temp_this and (not temp_other or temp_this.data <= temp_other.data):
                temp.next = Node(temp_this.data)
                temp_this = temp_this.next
            else:
                temp.next = Node(temp_other.data)
                temp_other = temp_other.next
            temp = temp.next
        self.head = merge_head.next
        return self

    def delete(self, key):
        super().delete(key)

    @classmethod
    def from_list(cls, lst: list):
        """
        Creates new sorted singly-linked list from a python list.
        :param lst:
        :return:
        """
        new_linked_list = cls()
        for item in lst:
            new_linked_list.insert(item)
        return new_linked_list

