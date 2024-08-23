# from typing import List   :(with or without using it we can run code)
def moveZeros(n: int,  a: [int]) -> [int]:
    j = -1
    # Place the pointer j
    for i in range(n):
        if a[i] == 0:
            j = i
            break
    
    # No non-zero elements
    if j == -1:
        return a
    
    # Move the pointers i and j and swap accordingly
    for i in range(j + 1, n):
        if a[i] != 0:
            a[i], a[j] = a[j], a[i]
            j += 1
    
    return a


arr = [1, 2, 3, 2,0,1,2,3,4,0,7,0,7,0,5,0,2]
n = len(arr)
ans = moveZeros(n, arr)
for s in ans:
    print(s, end=' ')
print()
