#Summation approach
def missingNumber(arr, N):
    # Summation of first N numbers:
    summation = (N * (N + 1)) // 2

    # Summation of all array elements:
    s2 = sum(arr)

    missingNum = summation - s2
    return missingNum

if __name__ == '__main__':
    arr = [1, 2, 4, 3]
    N = len(arr) +1
    ans = missingNumber(arr, N)
    print("The missing number is:", ans)

    
# XOR Approach:
def missingNumber(a, N):
    xor1 = 0
    xor2 = 0

    for i in range(N - 1):
        xor2 = xor2 ^ a[i]  # XOR of array elements
        xor1 = xor1 ^ (i + 1)  # XOR up to [1...N-1]
    
    xor1 = xor1 ^ N  # XOR up to [1...N]

    return xor1 ^ xor2  # the missing number


def main():
    N = 5
    a = [1, 2, 4, 5]
    ans = missingNumber(a, N)
    print("The missing number is:", ans)


if __name__ == '__main__':
    main()