def merge(arr, low, mid, high):
    """
    Merges two sorted subarrays into a single sorted array.
    Time Complexity: O(n)
    space complexity: O(n)
    Parameters:
    arr (list): The list to be sorted.
    low (int): The starting index of the first subarray.
    mid (int): The ending index of the first subarray.
    high (int): The ending index of the second subarray

    """
    tmp = []
    left = low
    right = mid + 1

    while (left <= mid and right <= high):
        if (arr[left] <= arr[right]):
            tmp.append(arr[left])
            left += 1
        else:
            tmp.append(arr[right])
            right += 1
    
    while left <= mid:
        tmp.append(arr[left])
        left += 1
    while right <= high:
        tmp.append(arr[right])
        right += 1
    
    for i in range(low, high + 1):
        arr[i] = tmp[i - low]



def ms(arr, low, high):
    """
    Recursively applies the merge sort algorithm to sort the array.
    Time Complexity:
    - Best/Average/Worst Case: O(n log n)
    Parameters:
    arr (list): The list to be sorted.
    low (int): The starting index of the segment to be sorted.
    high (int): The ending index of the segment to be sorted.
    """
    if low >= high:
        return
    mid = (low + high) // 2
    ms(arr, low, mid)
    ms(arr, mid + 1, high)
    merge(arr, low, mid, high)


def merge_sort(arr):
    """
    Sorts the list using the merge sort algorithm.
    Time Complexity: O(n log n)
    Parameters:
    arr (list): The list to be sorted.
    Returns:
    list: The sorted list.
    """
    ms(arr, 0, len(arr) - 1)
    return arr


# Testing array
arr = [12, 11, 13, 5, 6, 7]
print("Original array:", arr)
print("Sorted array:", merge_sort(arr))
# Output: [5, 6, 7, 11, 12, 13]