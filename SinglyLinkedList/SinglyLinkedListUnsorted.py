from SinglyLinkedList import SinglyLinkedList
from Node import Node


class SinglyLinkedListUnsorted(SinglyLinkedList):
    def __init__(self):
        super().__init__()

    def insert(self, data):
        node_new = Node(data)
        if self.head is not None:
            current = self.head
            while current.next:
                current = current.next
            current.next = node_new
        else:
            self.head = node_new

    def merge(self, other):
        if not (isinstance(other, type(self))):
            raise TypeError(f"This operation can only be performed with an object of type {type(self).__name__}.")
        else:
            current = self.head
            if current.head is None:
                return other
            if other.head is None:
                return current
            while current.next:
                current = current.next
            current.next = other.head
            return current

    def swap_index(self, ind1, ind2):
        if ind1 == ind2:
            return

        prev1 = None
        curr1 = self.head
        ind_curr1 = 0
        while curr1 is not None and ind_curr1 != ind1:
            prev1 = curr1
            curr1 = curr1.next
            ind_curr1 += 1

        prev2 = None
        curr2 = self.head
        ind_curr2 = 0
        while curr2 is not None and ind_curr2 != ind2:
            prev2 = curr2
            curr2 = curr2.next
            ind_curr2 += 1

        if curr1 is None or curr2 is None:
            return

        # If node 1 is not head of list 1
        if prev1 is not None:
            prev1.next = curr2
        else:  # make node 2 new head
            self.head = curr2

        # If node 2 is not head of list 2
        if prev2 is not None:
            prev2.next = curr1
        else:  # make node 1 new head
            self.head = curr1

        temp = curr1.next
        curr1.next = curr2.next
        curr2.next = temp

    def delete(self, key):
        super().delete(key)
