from SinglyLinkedList import SinglyLinkedListSorted
from MergeableHeap import MergeableHeap
from Node import Node

class MergeableHeapSorted(SinglyLinkedListSorted, MergeableHeap):

    def __init__(self):
        super().__init__()

    def insert(self, data):
        super().insert(data)

    def minimum(self):
        return self.head.data

    def extract_min(self):
        if self.head is not None:
            min = self.head
            if self.head.next is not None:
                self.head = min.next
            else:
                self.head = Node(None)
            return min
        else:
            raise KeyError("Heap is empty. There is no minimum.")

    def union(self, other):
        super().merge(other)
