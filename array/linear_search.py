from typing import List  
def linear(arr: List[int], num: int) -> int:
    
    for i in range (len(arr)):
        if (arr[i]==num):
            return i
    return -1

arr = [1,2,3,4,5]
num=5
ans = linear(arr,num)
print(ans)