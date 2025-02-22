def Insertion_sort(arr):
    """
        Insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time.
        Time Complexity: O(n^2) - Worst case - Best case: O(n)
        Space Complexity: O(1)
        :param arr: List of elements
        :return: Sorted list
    """
    n = len(arr)    
    for i in range(n):
        j = i
        while (j > 0 and arr[j - 1] > arr[j]):
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr

if __name__ == '__main__':
    array = [3, 2, 10,1]
    print(Insertion_sort(array))