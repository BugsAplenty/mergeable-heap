import unittest
from TestMergeableHeap import TestMergeableHeap
from MergeableHeap.MergeableHeapSorted import MergeableHeapSorted
from helper_functions import generate_random_list, display_list


class TestMergeableHeapSorted(TestMergeableHeap):
    def test_get_min(self):
        """
        Tests the get_min method for sorted heaps.
        :return:
        """
        for i in range(5):
            rand_list = generate_random_list(10, (0, 20))
            list_min = min(rand_list)
            heap_from_list = MergeableHeapSorted.from_list(rand_list)
            self.assertEqual(list_min, heap_from_list.minimum())

    def test_display(self):  # This doubles as a sorting test.
        """
        Tests the display method for sorted singly linked lists.
        :return:
        """
        for i in range(5):
            rand_list = generate_random_list(10, (0, 20))
            list_sorted = sorted(rand_list)
            list_display = display_list(list_sorted)
            heap_from_list = MergeableHeapSorted.from_list(rand_list)
            heap_display = heap_from_list.display()
            self.assertEqual(list_display, heap_display)

    def test_union(self):
        """
        Tests the union method for sorted heaps.
        :return:
        """
        for i in range(5):
            rand_list1 = generate_random_list(10, (0, 20))
            rand_list2 = generate_random_list(10, (0, 20))
            list_sorted = sorted(rand_list1 + rand_list2)
            list_display = display_list(list_sorted)
            heap_from_list1 = MergeableHeapSorted.from_list(rand_list1)
            heap_from_list2 = MergeableHeapSorted.from_list(rand_list2)
            heap_union = heap_from_list1
            heap_union.union(heap_from_list2)
            self.assertEqual(heap_union.display(), list_display)

    def test_insert(self):  # TODO: Write tests for the insert method.
        """
        Tests the insert method for sorted heaps.
        :return:
        """
        pass

    def test_extract_min(self):
        """
        Tests the extract_min method for sorted heaps.
        :return:
        """
        for i in range(5):
            rand_list = generate_random_list(10, (0, 20))
            heap_from_list = MergeableHeapSorted.from_list(rand_list)
            key_min = heap_from_list.extract_min()
            list_min = min(rand_list)
            list_without_min = rand_list
            list_without_min.remove(list_min)
            list_without_min_sorted = sorted(list_without_min)
            self.assertEqual(list_min, key_min)
            self.assertEqual(heap_from_list.display(), display_list(list_without_min_sorted))


if __name__ == '__main__':
    unittest.main()
