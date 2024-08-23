def intersection(arr1, arr2):
    # Ensure both arrays are sorted
    arr1.sort()
    arr2.sort()

    i, j = 0, 0
    result = []

    # Use two pointers to find common elements
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            # Found a common element, add it to result if it's not a duplicate
            if len(result) == 0 or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
            j += 1
    
    return result

# Example usage
arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 3, 5, 6, 7]

ans = intersection(arr1, arr2)
print("Intersection of arrays:", ans)
