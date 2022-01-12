from SinglyLinkedList import SinglyLinkedListSorted
from MergeableHeap import MergeableHeap
from Node import Node

class MergeableHeapSorted(SinglyLinkedListSorted, MergeableHeap):

    def __init__(self):
        super().__init__()

    def insert(self, data):
        super().insert(data)

    def minimum(self):
        """
        Returns the minimum key in a sorted min-heap.
        :return:
        """
        return self.head.data

    def extract_min(self):
        """
        Returns minimum from sorted min-heap and removes it from the heap.
        :return:
        """
        if self.head is not None:
            node_min = self.head
            if self.head.next is not None:
                self.head = node_min.next
            else:
                self.head = Node(None)
            return node_min.data
        else:
            raise KeyError("Heap is empty. There is no minimum.")

    def union(self, other):
        super().merge(other)
