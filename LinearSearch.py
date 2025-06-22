def linearSearch(arr, targetVal):
    for i in range(len(arr)):
        if arr[i] == targetVal:
            return f"{targetVal} found at index {i}"
    return f"{targetVal} not found in the array"