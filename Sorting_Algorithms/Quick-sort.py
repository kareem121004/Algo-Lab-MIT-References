
def partition(arr, low, high):
    """
    Partitions the array using the first element as the pivot.
    Moves elements smaller than or equal to the pivot to the left
    and elements greater than the pivot to the right.
    
    Time Complexity: O(n) (for partitioning a single segment)
    
    Parameters:
    arr (list): The list to be partitioned.
    low (int): The starting index of the segment to partition.
    high (int): The ending index of the segment to partition.

    Returns:
    int: The index position of the pivot after partitioning.
    """

    pivot = arr[low]
    i = low
    j = high

    while i < j:
        while (arr[i] <= pivot and i <= high - 1):
            i += 1
        while (arr[j] > pivot and j >= low + 1):
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j



def qs(arr, low, high):
    """
    Recursively applies the quicksort algorithm to sort the array.
    
    Time Complexity:
    - Best/Average Case: O(n log n)
    - Worst Case: O(n^2) (when the smallest or largest element is always chosen as the pivot)
    
    Parameters:
    arr (list): The list to be sorted.
    low (int): The starting index of the segment to be sorted.
    high (int): The ending index of the segment to be sorted.

    Returns:
    list: The sorted list.
    """

    if (low < high):
        partition_idx = partition(arr, low, high)
        qs(arr, low, partition_idx - 1)
        qs(arr, partition_idx + 1, high)
    return arr


def quick_sort(arr):
    """
    Sorts the given list using the QuickSort algorithm.
    
    Time Complexity:
    - Best/Average Case: O(n log n)
    - Worst Case: O(n^2) (when the smallest or largest element is always chosen as the pivot)
    
    Parameters:
    arr (list): The list to be sorted.

    Returns:
    list: The sorted list.
    """
    new_arr = qs(arr, 0, len(arr) - 1)
    return new_arr

# Testing array
arr = [7, 5, 3, 2, 9, -1]
print(quick_sort(arr))
