# utils/algorithms.py
# Implementasi algoritma pencarian dan pengurutan

def quick_sort(arr, key, ascending=True):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if (x[key] < pivot[key] if ascending else x[key] > pivot[key])]
    middle = [x for x in arr if x[key] == pivot[key]]
    right = [x for x in arr if (x[key] > pivot[key] if ascending else x[key] < pivot[key])]
    
    return quick_sort(left, key, ascending) + middle + quick_sort(right, key, ascending)

def binary_search(arr, key, value):
    # Pastikan array sudah diurutkan
    arr = quick_sort(arr, key)
    
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid][key] == value:
            return arr[mid]
        elif arr[mid][key] < value:
            low = mid + 1
        else:
            high = mid - 1
    
    return None