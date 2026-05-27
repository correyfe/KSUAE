def bubble_sort(arr):
    compare_count = 0
    swap_count = 0
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                swap_count += 1
                compare_count += 1
            else:
                compare_count += 1
        if not swapped:
            break
    return swap_count, compare_count
