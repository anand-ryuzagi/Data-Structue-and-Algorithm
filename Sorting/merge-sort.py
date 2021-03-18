# mergesort = it is divide and conquer method in which a single problem is divided in to small problem of same type and after solving each small problem combine the solution.
# Time complexity : O(nlogn)
# Space complexity : O(n)

# algorithms :
# 1. divide the array into two equal halves 
# 2. recursively  divide each sub arrays into two halves until length of last subarray is equal to 1.
# 3. after that apply merge function to join the solution of all the problems.

def merge(a,b,arr):
    len_a= len(a)
    len_b = len(b)
    i = 0
    j = 0
    k = 0
    while i<len_a and j<len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i +=1
        else:
            arr[k] = b[j]
            j+=1
        k += 1

    while i<len_a:
        arr[k] = a[i]
        i += 1
        k += 1
    while j<len_b:
        arr[k] = b[j]
        j += 1
        k += 1

def mergeSort(arr):
    if len(arr) <= 1:
        return 
    
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    mergeSort(left)
    mergeSort(right)

    merge(left, right, arr)

arr =[1,5,2,3,9,7,0]
mergeSort(arr)
print(arr)
