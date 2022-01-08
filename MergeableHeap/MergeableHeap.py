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



