from SinglyLinkedList import SinglyLinkedListUnsorted
from MergeableHeap import MergeableHeap
from Node import Node


class MergeableHeapUnsorted(SinglyLinkedListUnsorted, MergeableHeap):

    def __init__(self):
        super().__init__()

    def insert(self, data):
        """
        Inserts a new node into a min-heap.
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

    def minimum(self):
        """
        Returns the minimum key in an unsorted min-heap.
        :return:
        """
        return self.head.data

    def extract_min(self):
        """
        Returns the minimum key in an unsorted min-heap and removes it from the heap.
        :return:
        """
        if self.head is not None:
            key_min = self.minimum()
            if self.head.next is not None:
                current = self.head
                key_second_min = self[1].data
                ind_second_min = 1
                for i in range(1, self.length()):
                    if key_second_min > self[i].data:
                        key_second_min = self[i].data
                        ind_second_min = i
                self.head.data = key_second_min
                self[ind_second_min].data = self[self.length() - 1].data
                self.delete_at(self.length() - 1)
                self.min_heapify(ind_second_min)
            else:
                self.head = None
            return key_min
        else:
            raise Exception("Heap is empty. There is no minimum.")

    def min_heapify(self, i):  # TODO: This doesn't work properly. Some debugging is needed.
        """
        Performs the min-heapify routine recursively starting with the i-th node in the heap.
        :param i:
        :return:
        """
        l = self[2 * i].data
        r = self[2 * i + 1].data
        p = self[i].data
        smallest = i
        if self[2 * i] is not None and l < p:
            smallest = 2 * i
        if self[2 * i + 1] is not None and r < self[smallest].data:
            smallest = 2 * i + 1
        if smallest != i:
            self.swap_index(i, smallest)
            self.min_heapify(i)

    def union(self, other):
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
