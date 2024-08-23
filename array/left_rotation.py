#left rotation 
'''
def left(arr,n):
    temp = arr[0]
    temp1 = arr[1]
    temp2 = arr[2]
    temp3 = arr[3]
    for i in range (n-4):
        arr[i] = arr[i+4]
    arr[n-4]=temp
    arr[n-3] = temp1
    arr[n-2] = temp2
    arr[n-1] = temp3
    
    for i in range(n):
        print(arr[i],end = " ")
arr = [1,2,3,4,5,6,7]
n = len(arr)
left(arr,n)
#right rotation by own method
  '''
def right(arr,n):
    temp = arr[n-1]
    for i in range(n-2,-1,-1):
        arr[i+1] = arr[i]
    arr[0] = temp
    for i in range(n):
        print(arr[i],end = " ")
arr = [1,2,3,4,5]
n = 5
right(arr,n) 

''' 
#left rotation
def left(arr , n):
    temp = arr[0]
    for i in range(n-1):
        arr[i]=arr[i+1]
    arr[n-1]=temp

    for i in range(n):
        print(arr[i],end = " ")   
arr = [1,2,3,4,5]
n = 5
left(arr,n)
'''