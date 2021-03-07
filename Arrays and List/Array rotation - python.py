#time complexity = O(n)

def rotate(arr,n,d):
    for i in range(d):
        rotateleftbyone(arr,n)

def rotateleftbyone(arr,n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    
    arr[n-1] = temp

arr = [1,2,3,4,5,6]
print(f"array before rotation {arr}")
rotate(arr,6,4)
print(f"array after rotation {arr}")
