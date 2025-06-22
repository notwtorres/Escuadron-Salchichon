def binarySearch(arr, targetVal):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == targetVal:
            return f"{targetVal} found at index {mid}"
        
        if arr[mid] < targetVal:
            left = mid + 1
        else:
            right = mid - 1

    return f"{targetVal} not found in the array"