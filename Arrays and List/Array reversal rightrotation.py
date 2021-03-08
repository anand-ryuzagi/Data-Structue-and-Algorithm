#time complexity = O(n)
def rotate(arr,n,d):
    reverseArray(arr,0,n-d-1)
    reverseArray(arr,n-d,n-1)
    reverseArray(arr,0,n-1)

def reverseArray(arr,start,end):
    while (start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1

arr = [1,2,3,4,5,6,7]
print(f"array before rotation {arr}")
rotate(arr,7,2)
print(f"array after rotation {arr}")
