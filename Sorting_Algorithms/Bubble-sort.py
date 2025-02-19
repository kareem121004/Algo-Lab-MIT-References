def Bubble_sort(arr):
    """
        Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.
        Time Complexity: O(n^2) - Worst case - Best case: O(n)
        Space Complexity: O(1)
        :param arr: List of elements
        :return: Sorted list
        Optimization: If the array is already sorted, then the algorithm will stop.
    """
    n = len(arr)
    for i in range(n):
        flag = 0
        for j in range(n - i - 1):
            if (arr[j] > arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = 1
            
        if (flag == 0):
            break
    return arr



if __name__ == '__main__':
    array = [3, 2, 10,1]
    print(Bubble_sort(array))