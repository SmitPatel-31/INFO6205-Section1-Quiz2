def binary_search_rotated(arr, target, rotation_index):

    if not arr:
        return False

    arr_size = len(arr)

    if rotation_index == 0:
        return binary_search(arr, 0, arr_size - 1, target)

    if target >= arr[0]:  
        return binary_search(arr, 0, rotation_index - 1, target)
    else:  # Search in right part (after rotation)
        return binary_search(arr, rotation_index, arr_size - 1, target)

def binary_search(arr, left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False
