def selection_sort(arr):
    compare_count = 0
    swap_count = 0
    n = len(arr)
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            compare_count += 1
            if arr[j] < arr[min_idx]:
                min_idx = j

        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swap_count += 1
    
    return swap_count, compare_count


def bidirectional_selection_sort(arr):
    compare_count = 0
    swap_count = 0
    n = len(arr)
    left = 0
    right = n - 1
    
    while left < right:
        min_idx = left
        max_idx = right

        for i in range(left, right + 1):
            compare_count += 1
            if arr[i] < arr[min_idx]:
                min_idx = i
            
            compare_count += 1
            if arr[i] > arr[max_idx]:
                max_idx = i
        
        if min_idx != left:
            arr[left], arr[min_idx] = arr[min_idx], arr[left]
            swap_count += 1
        
        # Размещаем максимум в конец
        # Важно: если max_idx был равен left, то мы его уже переместили!
        if max_idx == left:
            max_idx = min_idx
        
        if max_idx != right:
            arr[right], arr[max_idx] = arr[max_idx], arr[right]
            swap_count += 1
        
        left += 1
        right -= 1
    
    return swap_count, compare_count
