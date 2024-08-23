def isSorted(arr, n):
    for i in range(n):
        if arr[i] < arr[i - 1]:
            return False
    return True

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    print("True" if isSorted(arr, n) else "False")