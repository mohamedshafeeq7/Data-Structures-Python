def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        # Flag to optimize the algorithm by stopping if no swaps are made in a pass
        swapped = False
        
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swaps are made in a pass, the array is already sorted
        if not swapped:
            break

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array:", arr)  # Output: [11, 12, 22, 25, 34, 64, 90]
