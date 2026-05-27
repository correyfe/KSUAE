from random import randint
import time
from A_part.bubble import bubble_sort
from A_part.selection import selection_sort, bidirectional_selection_sort


def create_arrays():
    random_array = [randint(1, 10000) for _ in range(10000)]
    
    near_sorted = [i for i in range(10000)]
    for _ in range(250):
        idx1 = randint(0, 9999)
        idx2 = randint(0, 9999)
        near_sorted[idx1], near_sorted[idx2] = near_sorted[idx2], near_sorted[idx1]

    reversed_array = [i for i in range(10000, 0, -1)]
    
    return random_array, near_sorted, reversed_array

def test_sorting_algorithm(algorithm_name, sort_func, arrays):
    arr_types = ["Случайные числа(ns): ", "Почти отсортированные(ns): ", "Обратный порядок(ns): "]
    
    print("=" * 60)
    print(algorithm_name)
    print("=" * 60)
    for i in range(len(arr_types)):
        arr_copy = arrays[i].copy()
        start_time = time.time_ns()
        swaps, compares = sort_func(arr_copy)
        end_time = time.time_ns()
        print(arr_types[i], end_time - start_time, '\n',
              "Количество сравнений:", compares,
              "Количество перестановок:", swaps, '\n')

def main():
    arrs = create_arrays()
    
    test_sorting_algorithm("Пузырьковая сортировка", bubble_sort, arrs)
    test_sorting_algorithm("Сортировка выбором (базовая версия)", selection_sort, arrs)
    test_sorting_algorithm("Двусторонняя сортировка выбором", bidirectional_selection_sort, arrs)

if __name__ == "__main__":
    main()