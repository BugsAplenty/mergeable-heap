from MergeableHeap import MergeableHeapSorted, MergeableHeapUnsorted
from enum import Enum


class States(Enum):
    TYPE_SELECT = 1
    OPERATION_SELECT = 2
    CHOOSE_HEAP = 3
    CHOOSE_OTHER_HEAP = 4
    CHOOSE_ELEM = 5


class Interface:
    def __init__(self):
        self.chosen_operation = None
        self.state = States.TYPE_SELECT
        self.heaps = []
        self.input = None
        self.chosen_type = None
        self.chosen_heap = None
        self.chosen_heap_other = None

    def dialogue(self):
        if self.state == States.TYPE_SELECT:
            print(f"Choose data structure: \n"
                  "1 - Sorted mergeable heap \n"
                  "2 - Unsorted mergeable heap \n"
                  "3 - Unsorted mergeable heap with disjoint sets \n")
            # self.chosen_type = self.input
        elif self.state == States.OPERATION_SELECT:
            print("Which operation would you like to perform? \n"
                  "1 - Show heaps \n"
                  "2 - Make heap \n"
                  "3 - Insert element \n"
                  "4 - Get minimum \n"
                  "5 - Extract minimum \n"
                  "6 - Union with other set \n"
                  "7 - Execute list of commands from text file \n"
                  "R - Reset \n")
            # self.chosen_operation = self.input
        elif self.state == States.CHOOSE_HEAP:
            print(f"Which heap would you like to perform this operation on? \n"
                  f"{self.display_all_heaps()} \n"
                  f"R - Reset")
        elif self.state == States.CHOOSE_OTHER_HEAP:
            print(f"Which heap would you like to join with this? \n"
                  f"{self.display_all_heaps()} \n"
                  f"R - Reset")

        elif self.state == States.CHOOSE_ELEM:
            print("Type in the number you'd like to add: \n"
                  "R - Reset")

    def run(self):
        while True:
            self.dialogue()
            self.input = input()
            if self.state == States.TYPE_SELECT:
                self.chosen_type = self.input
                self.state = States.OPERATION_SELECT
            elif self.state == States.OPERATION_SELECT:
                self.chosen_operation = self.input
                match self.chosen_operation:
                    case 1:
                        self.display_all_heaps()
                    case 2:
                        if self.chosen_type == 1:
                            self.heaps.append(MergeableHeapSorted())
                        else:
                            self.heaps.append(MergeableHeapUnsorted())
                    case 3:



    def display_all_heaps(self):
        for ind, heap in enumerate(self.heaps):
            heap_list_string = f'{ind} - {heap.display() if heap.display else "Empty"} \n'
            return heap_list_string

