import time
import random

def insertion_sort(arr):
    """Insertion Sort Algorithm"""
    arr = arr[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:  # Shift elements to make space for key
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Place key in its correct position
    return arr

def merge_sort(arr):
    """Merge Sort Algorithm"""
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])  # Recursively sort left half
    right_half = merge_sort(arr[mid:])  # Recursively sort right half
    
    return merge(left_half, right_half)

def merge(left, right):
    """Merge two sorted halves"""
    sorted_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr

def heapify(arr, n, i):
    """Heapify function for Heapsort"""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)  # Recursively heapify affected subtree

def heap_sort(arr):
    """Heapsort Algorithm"""
    arr = arr[:]
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):  # Build max heap
        heapify(arr, n, i)
    
    for i in range(n - 1, 0, -1):  # Extract elements from heap
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

def quick_sort(arr):
    """Quicksort Algorithm"""
    if len(arr) <= 1:
        return arr[:]
    pivot = arr[len(arr) // 2]  # Choose middle element as pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def generate_datasets():
    """Generate various datasets for sorting analysis"""
    sizes = [10, 100, 1000, 10000, 50000]  # Different dataset sizes
    datasets = {}
    for size in sizes:
        random_list = [random.randint(1, 10000) for _ in range(size)]
        datasets[f'Random_{size}'] = random_list
        datasets[f'Sorted_{size}'] = sorted(random_list)
        datasets[f'Reverse_{size}'] = sorted(random_list, reverse=True)
    return datasets

def analyze_sorting_algorithms():
    """Run and compare sorting algorithms on different datasets"""
    datasets = generate_datasets()
    sorting_algorithms = {
        'Insertion Sort': insertion_sort,
        'Merge Sort': merge_sort,
        'Heapsort': heap_sort,
        'Quicksort': quick_sort
    }
    
    results = {}
    for dataset_name, data in datasets.items():
        results[dataset_name] = {}
        for sort_name, sort_function in sorting_algorithms.items():
            start_time = time.time()
            sorted_arr = sort_function(data)  # Ensuring no modification of original data
            end_time = time.time()
            results[dataset_name][sort_name] = end_time - start_time
    
    print("Sorting Performance Analysis (Time in seconds):")
    for dataset, timings in results.items():
        print(f"\nDataset: {dataset}")
        for sort_name, time_taken in timings.items():
            print(f"{sort_name}: {time_taken:.6f} sec")

# Run analysis
if __name__ == "__main__":
    analyze_sorting_algorithms()
