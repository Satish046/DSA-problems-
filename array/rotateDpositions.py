def reverse(arr, start, end):
    """Reverse the elements of arr from index start to end."""
    while start <= end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_left(arr, k):
    """Rotate the array arr to the left by k positions."""
    n = len(arr)
    k %= n  # Handle cases where k >= n
    
    # Reverse the first k elements
    reverse(arr, 0, k - 1)
    # Reverse the remaining n-k elements
    reverse(arr, k, n - 1)
    # Reverse the whole array
    reverse(arr, 0, n - 1)

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    rotate_left(arr, k)
    print("After rotating the array to the left by k positions:")
    print(arr)
