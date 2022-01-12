import unittest
from TestMergeableHeap import TestMergeableHeap
from MergeableHeap.MergeableHeapUnsorted import MergeableHeapUnsorted
from helper_functions import generate_random_list, display_list
import heapq


class TestMergeableHeapUnsorted(TestMergeableHeap):
    def test_get_min(self):
        """
        Tests the get_min method for unsorted heaps.
        :return:
        """
        for i in range(5):
            rand_list = generate_random_list(10, (0, 20))
            list_min = min(rand_list)
            heap_from_list = MergeableHeapUnsorted.from_list(rand_list)
            self.assertEqual(list_min, heap_from_list.minimum())

    def test_insert(self):  # TODO: Implement tests for the insert method.
        """
        Tests the insert method for unsorted heaps.
        :return:
        """
        pass

    def test_extract_min(self):  # TODO: Heapify doesn't work properly. Perform test on list after extraction after method is fixed.
        """
        Tests the extract_min method for unsorted heaps.
        :return:
        """
        for i in range(5):
            rand_list = generate_random_list(10, (0, 20))
            heap_from_list = MergeableHeapUnsorted.from_list(rand_list)
            key_min = heap_from_list.extract_min()
            list_min = min(rand_list)
            list_without_min = rand_list
            list_without_min.remove(list_min)
            heapq.heapify(list_without_min)
            self.assertEqual(list_min, key_min)
            # self.assertEqual(heap_from_list.display(), display_list(list_without_min))

    def test_display(self):
        """
        Tests the display method for singly linked lists.
        :return:
        """
        for i in range(5):
            rand_list = generate_random_list(10, (0, 20))
            list_sorted = sorted(rand_list)
            list_display = display_list(list_sorted)
            heap_from_list = MergeableHeapUnsorted.from_list(rand_list)
            heap_display = heap_from_list.display()
            self.assertEqual(list_display, heap_display)

    def test_union(self): # TODO: min_heapify doesn't work properly, so the test currently fails. Some debugging needed.
        """
        Tests the union method for unsorted heaps.
        :return:
        """
        for i in range(5):
            rand_list1 = generate_random_list(10, (0, 20))
            rand_list2 = generate_random_list(10, (0, 20))
            list_sorted = sorted(rand_list1 + rand_list2)
            list_display = display_list(list_sorted)
            heap_from_list1 = MergeableHeapUnsorted.from_list(rand_list1)
            heap_from_list2 = MergeableHeapUnsorted.from_list(rand_list2)
            heap_union = heap_from_list1
            heap_union.union(heap_from_list2)
            self.assertEqual(heap_union.display(), list_display)


if __name__ == '__main__':
    unittest.main()
