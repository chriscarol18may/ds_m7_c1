def reverse_array(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        # Swap elements at start and end
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return arr


# Example:
arr = [1, 2, 3, 4, 5]
print("Original:", arr)
print("Reversed:", reverse_array(arr))