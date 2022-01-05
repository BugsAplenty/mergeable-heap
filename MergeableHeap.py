from SinglyLinkedList import SinglyLinkedList
from abc import ABC, abstractmethod


class MergeableHeap(ABC, SinglyLinkedList):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def minimum(self):
        pass

    @abstractmethod
    def insert(self, data):
        pass

    @abstractmethod
    def extract_min(self):
        pass

    @abstractmethod
    def union(self, other):
        pass


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


class MergeableHeapUnsorted(SinglyLinkedListUnsorted, MergeableHeap):

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

    def minimum(self):
        return self.head.data

    def extract_min(self):
        if self.head is not None:
            key_min = self.head
            if self.head.next is not None:
                current = self.head
                key_second_min = self[1]
                ind_second_min = 1
                for i in range(self.length())[1:]:
                    if key_second_min > self[i]:
                        key_second_min = self[i]
                        ind_second_min = i
                self.head.data = key_second_min
                self[ind_second_min].data = self[self.length()].data
                self.delete(self[self.length()].data)
                self.min_heapify(self[ind_second_min])
            else:
                self.head = None
            return key_min
        else:
            raise Exception("Heap is empty. There is no minimum.")

    def min_heapify(self, i):
        l = self[2 * i].data
        r = self[2 * i + 1].data
        p = self[i].data
        smallest = i
        if self[2 * i] is not None and l < p:
            smallest = 2 * i
        if self[2 * i + 1] is not None and r < self[smallest]:
            smallest = 2 * i + 1
        if smallest != i:
            self.swap_index(i, smallest)
            self.min_heapify(i)

    def union(self):
        raise NotImplementedError
