import random


def generate_random_list(size: int, nrange: tuple) -> list:
    """
    Generates list of random integers within desired range.
    :param size: Size of list.
    :param nrange: Range of integers from which to select randomly.
    :return:
    """
    rand_list = []
    for i in range(size):
        n = random.randint(nrange[0], nrange[1])
        rand_list.append(n)
    return rand_list


def display_list(lst: list) -> str:
    """
    Returns string of list items in similar format to MergeableHeap object.
    :param lst:
    :return:
    """
    list_str = str(lst[0])
    for item in lst[1:]:
        list_str += f" -> {item}"
    return list_str
