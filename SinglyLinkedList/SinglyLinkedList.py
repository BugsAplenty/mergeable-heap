from abc import ABC, abstractmethod


class SinglyLinkedList(ABC):
    def __init__(self):
        self.head = None

    def __getitem__(self, ind):
        current = self.head
        index_current = 0
        if self.head is None:
            print("List is empty.")
            return None
        while current.next:
            if index_current == ind:
                return current.data
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
        return

    def delete(self, key):
        current = self.head
        if current.head is not None:
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

    def length(self):
        if self.head is None:
            print("The list is empty.")
        else:
            current = self.head
            count = 0
            while current.next:
                count += 1
            return count

    def display(self):
        list_str = ""
        if self.head is None:
            return list_str
        else:
            current = self.head
            list_str += str(current.data)
            while current.next:
                list_str += f" -> {current.data}"
                current = current.next
            return list_str
