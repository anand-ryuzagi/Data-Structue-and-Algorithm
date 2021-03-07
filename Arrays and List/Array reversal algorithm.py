#time complexity = O(n)
#Let AB are the two parts of the input array where A = arr[0..d-1] and B = arr[d..n-1]. The idea of the algorithm is : 
#Reverse A to get ArB, where Ar is reverse of A.
#Reverse B to get ArBr, where Br is reverse of B.
#Reverse all to get (ArBr) r = BA.

def rotate(arr,n,d):
    reverseArray(arr,0,d-1)
    reverseArray(arr,d,n-1)
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
