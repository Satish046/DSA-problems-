def getSingleElement(arr):
    # XOR all the elements:
    xorr = 0
    for num in arr:
        xorr ^= num
    return xorr

def main():
    arr = [4, 1, 2, 1, 2,4,2,2,6]
    ans = getSingleElement(arr)
    print("The single element is:", ans)

if __name__ == "__main__":
    main()