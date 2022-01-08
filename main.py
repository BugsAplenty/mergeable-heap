from MergeableHeap import MergeableHeapSorted, MergeableHeapUnsorted
from enum import Enum
import sys

class States(Enum):
    TYPE_SELECT = 1
    OPERATION_SELECT = 2
    CHOOSE_HEAP = 3
    CHOOSE_OTHER_HEAP = 4
    CHOOSE_ELEM = 5

class Operations(Enum):
    SHOW_HEAPS = 1
    MAKE_HEAP = 2
    INSERT_ELEM = 3
    GET_MIN = 4
    EXTRACT_MIN = 5
    UNION = 6


class Interface:
    def __init__(self):
        self.chosen_operation = None
        self.state = States.TYPE_SELECT
        self.heaps = []
        self.input = None
        self.chosen_type = None
        self.chosen_heap = None
        self.chosen_heap_other = None
        self.chosen_insert = None

    def dialogue(self):
        if self.state == States.TYPE_SELECT:
            print(f"Choose data structure: \n"
                  "1 - Sorted mergeable heap \n"
                  "2 - Unsorted mergeable heap \n"
                  "3 - Unsorted mergeable heap with disjoint sets \n")
            # self.chosen_type = self.input
        elif self.state == States.OPERATION_SELECT:
            print(f"Which operation would you like to perform? \n"
                  f"{Operations.SHOW_HEAPS.value} - Show heaps \n"
                  f"{Operations.MAKE_HEAP.value} - Make heap \n"
                  f"{Operations.INSERT_ELEM.value} - Insert element \n"
                  f"{Operations.GET_MIN.value} - Get minimum \n"
                  f"{Operations.EXTRACT_MIN.value} - Extract minimum \n"
                  f"{Operations.UNION.value} - Union with other set \n"
                  # "7 - Execute list of commands from text file \n"
                  f"R - Reset \n"
                  f"Q - Quit \n")
            # self.chosen_operation = self.input
        elif self.state == States.CHOOSE_HEAP:
            print(f"Which heap would you like to perform this operation on? \n"
                  f"{self.display_all_heaps()} \n"
                  f"R - Reset \n"
                  f"Q - Quit \n")
        elif self.state == States.CHOOSE_OTHER_HEAP:
            print(f"Which heap would you like to join with this? \n"
                  f"{self.display_all_heaps()} \n"
                  f"R - Reset \n"
                  f"Q - Quit")
        elif self.state == States.CHOOSE_ELEM:
            print("Type in the number you'd like to add: \n"
                  "R - Reset \n"
                  "Q - Quit")

    def process_input(self):
        if self.input == "R":
            self.reset()
        elif self.input == "Q":
            sys.exit()
        else:
            try:
                input_processed = int(self.input)
                return input_processed
            except ValueError:
                print("Invalid input. \n")

    def run(self):
        while True:
            self.dialogue()
            self.input = input()
            # Tier 1
            if self.state == States.TYPE_SELECT:
                self.chosen_type = self.process_input()
                if self.chosen_type in (1,2,3): # TODO: Replace 1,2,3 with some kind of enumeration of possible classes.
                    self.state = States.OPERATION_SELECT
                else:
                    print("Selection out of bounds. \n")

            # Tier 2
            elif self.state == States.OPERATION_SELECT:
                self.chosen_operation = self.process_input()
                if self.chosen_operation in (1,2,3,4,5,6):
                    if self.chosen_operation == Operations.SHOW_HEAPS.value:
                        self.display_all_heaps()
                        self.back_to_operations_select()
                    elif self.chosen_operation == Operations.MAKE_HEAP.value:
                        if self.chosen_type == 1:
                            self.heaps.append(MergeableHeapSorted())
                        else:
                            self.heaps.append(MergeableHeapUnsorted())
                            self.back_to_operations_select()
                    else:
                        self.state = States.CHOOSE_HEAP


            # Tier 3
            elif self.state == States.CHOOSE_HEAP:
                self.chosen_heap = self.process_input()
                if self.chosen_heap in range(len(self.heaps)):
                    match self.chosen_operation:
                        case Operations.INSERT_ELEM.value:
                            self.state = States.CHOOSE_ELEM
                        case Operations.GET_MIN.value:
                            print(self.heaps[self.chosen_heap].minimum())
                            self.back_to_operations_select()
                        case Operations.EXTRACT_MIN.value:
                            key_min = self.heaps[self.chosen_heap].extract_min()
                            print(f"Minimum is: {key_min}. \n"
                                  f"Heap is now: {self.heaps[self.chosen_heap]}")
                            self.back_to_operations_select()
                        case Operations.UNION.value:
                            self.state = States.CHOOSE_OTHER_HEAP
                else:
                    print("Invalid input. Try again. \n")

            # Tier 4
            elif self.state == States.CHOOSE_ELEM:
                    self.heaps[self.chosen_heap].insert(self.chosen_insert)
                    self.back_to_operations_select()
            elif self.state == States.CHOOSE_OTHER_HEAP:
                self.chosen_heap_other = self.process_input()
                if self.chosen_heap_other in range(len(self.heaps)):
                    self.heaps[self.chosen_heap].union(self.heaps[self.chosen_heap_other])
                    self.back_to_operations_select()

    def display_all_heaps(self):
        heap_list_str = ""
        if self.heaps:
            for ind, heap in enumerate(self.heaps):
                heap_list_str += f'{ind} - {heap.display() if heap.display() else "Empty"} \n'
        print(heap_list_str)

    def reset(self):
        self.chosen_operation = None
        self.state = States.TYPE_SELECT
        self.heaps = []
        self.input = None
        self.chosen_type = None
        self.chosen_heap = None
        self.chosen_heap_other = None
        self.chosen_insert = None

    def back_to_operations_select(self):
        self.chosen_operation = None
        self.state = States.OPERATION_SELECT
        self.input = None
        self.chosen_heap = None
        self.chosen_heap_other = None
        self.chosen_insert = None

if __name__ == "__main__":
    interface = Interface()
    interface.run()

