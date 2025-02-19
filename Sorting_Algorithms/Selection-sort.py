
def Selection_sort(arr):
     """
        Selection sort is a simple sorting algorithm that selects the smallest element from an unsorted list in each iteration and places that element at the beginning of the unsorted list.
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        :param arr: List of elements
        :return: Sorted list
     """
     n = len(arr)
     for i in range (n):
        min_index = i
        for j in range (i + 1, n):
            if (arr[j] < arr[min_index]):
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
     return arr


if __name__ == '__main__':
    array = [3, 2, 10,1]
    print(Selection_sort(array))