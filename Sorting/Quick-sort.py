# Quicksort: in this sorting a pivot point is selected first and using this pivot the whole array is partitioned in such a way that all datas in the left are samller than pivot value and all the data in the right are greater than pivot value. after this the sorting algorithm is then appplied to the sub arrays recursively.
# Time complexity : average case : O(nlogn)
#                 : worst case : O(n^2)
# Space complexity : O(logn)

# algorithm:
# 1. a pivot is slelected at end and initialize i and j value where i starts with -1 and j iterates from left to pivot point.
# 2. at each value of j it is compared with  the pivot whether it is small and if it small it is swap with value at index i+1 and it it not j moves to next wihtout swapping.
# 3. at the end of the iteration the pivot value is swapped with value at index i+1
# 4. the process is then recursively use for sub array.

def partition(arr,start,end):
    i = start -1
    pivot = arr[end]

    for j in range(start,end):
        if(arr[j]<pivot):
            i += 1
            swap(i,j,arr)
    swap(i+1,end,arr)
    return i+1
    
    
def quicksort(arr,start,end):
    if(start<end):
        pindex = partition(arr,start,end)
        quicksort(arr,start,pindex-1)
        quicksort(arr,pindex+1,end)

def swap(a,b,arr):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

if __name__ == __main__:
  arr = [2,1,9,6,3,4]
  quicksort(arr,0,5)
  print(arr)
