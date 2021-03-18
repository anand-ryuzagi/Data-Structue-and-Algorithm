# Heapsort : it uses max heap order then switch the value at index 0 to index size and heapify or rearrange the heap in max order heap. the process is repeated until size become 0.

# Time complexity : O(nlogn)
# Space complexity : O(1)

def buildHeap(arr,size):
    for i in range(size//2,-1,-1):
        heapify(arr,i,size)

def heapify(arr,index,size):
    left = 2*index + 1
    right = left +1
    max = index

    if left < size and arr[left] > arr[max]:
        max = left

    if right< size and arr[right] > arr[max]:
        max = right
    
    if index!=max:
        swap(index,max,arr)
        heapify(arr,max,size)

def swap(a,b,arr):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

def heapSort(arr,size):
    buildHeap(arr,size)


    while size > 0:
        swap(0,size-1,arr)
        size -= 1
        heapify(arr,0,size)

arr = [1,4,2,3,9,5,6,7]
heapSort(arr,8)
print(arr)
