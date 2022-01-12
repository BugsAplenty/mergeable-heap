from abc import ABC, abstractmethod
from Node import Node


class SinglyLinkedList(ABC):
    def __init__(self):
        self.head = None

    def __getitem__(self, ind: int):
        """
        Allows pythonic indexing of singly-linked lists.
        :param ind:
        :return:
        """
        current = self.head
        index_current = 0
        if self.head is None:
            print("List is empty.")
            return None
        while current:
            if index_current == ind:
                return current
            else:
                current = current.next
                index_current += 1
        print("Index out of bounds.")
        return None

    # def __setitem__(self, ind, data):
    #     if ind > self.length() - 1:
    #         raise Exception
    #     current = self.head
    #     for i in range(ind):
    #         current = current.next
    #     current.data = data

    @abstractmethod
    def insert(self, data):
        pass

    def delete(self, key: int):
        """
        Deletes from singly-linked list by key.
        :param key: Key to be deleted.
        :return:
        """
        current = self.head
        if current is not None:
            if current.data == key:
                self.head = current.next
                return
        while current.next:
            if current.data == key:
                break
            prev = current
            current = current.next

        if current is None:
            print("Requested key not found.")
            return
        prev.next = current.next

    def delete_at(self, ind: int):
        """
        Deletes node from singly-linked list by index.
        :param ind: Index of node to be deleted.
        :return:
        """
        current = self.head
        if current is not None:
            if ind == 0:
                self.head = current.next
                return
        ind_current = 0
        while ind_current != ind:
            if current is None:
                print("Index out of bounds.")
                return
            else:
                prev = current
                current = current.next
                ind_current += 1
        prev.next = current.next

    def length(self):
        """
        Returns the length of the singly-linked list.
        :return:
        """
        if self.head is None:
            print("The list is empty.")
        else:
            current = self.head
            count = 0
            while current:
                count += 1
                current = current.next
            return count

    def display(self):
        """
        Displays the singly-linked list as a string.
        :return:
        """
        list_str = ""
        if self.head is None:
            return list_str
        else:
            current = self.head
            list_str += str(current.data)
            while current.next:
                list_str += f" -> {current.next.data}"
                current = current.next
            return list_str

    @abstractmethod
    def merge(self, other):
        pass

    @abstractmethod
    def from_list(self, lst):
        pass
