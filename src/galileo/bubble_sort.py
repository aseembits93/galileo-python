from typing import Union


def sorter(arr: Union[list[int], list[float]]) -> Union[list[int], list[float]]:
    # Use the built-in sort for better performance than bubble sort
    arr.sort()
    return arr
