
def binary_search(arr, val):
    """Locate the largest element less than or equal to `val` in `arr`.

    Assumes that `arr` is sorted. If `val` is smaller than all elements in the
    array or the array is empty, returns -1.

    Examples:
    >>> binary_search([], 10.0)
    -1

    >>> binary_search([1, 9, 16, 17], 15)
    1

    >>> binary_search([0, 3, 10, 12], -2)
    -1

    >>> binary_search([-5, 4, 12, 17], 17)
    3
    """
    if not arr:
        return -1  # Return -1 if the array is empty

    left, right = 0, len(arr) - 1
    result = -1  # Variable to store the index of the largest element <= val

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= val:
            result = mid  # Found a valid candidate, update result
            left = mid + 1  # Try to find a larger element less than or equal to val
        else:
            right = mid - 1  # Search on the left half

    return result