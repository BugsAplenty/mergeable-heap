import unittest
from abc import ABC, abstractmethod
from helper_functions import generate_random_list
from MergeableHeap import MergeableHeap

class TestMergeableHeap(unittest.TestCase, ABC):

    @abstractmethod
    def test_get_min(self):
        pass

    @abstractmethod
    def test_display(self):
        pass

    @abstractmethod
    def test_insert(self):
        pass

    @abstractmethod
    def test_extract_min(self):
        pass

    @abstractmethod
    def test_union(self):
        pass


if __name__ == '__main__':
    unittest.main()
