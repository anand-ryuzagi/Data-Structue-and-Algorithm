# Binary Heap : it is complete binary tree which maintains the heap order. it is used to create prioritized queue. Heap order may be of min or max. 

# Min heap : each parent node will have minimum value than the all children node. Also, the root node will have the least of all the value in the heap so that we can access minimum priortized value at constant time.

# Min heap : each parent node will have maximum value than the all children node. Also, the root node will have the max of all the value in the heap so that we can access maximum priortized value at constant time.

def buildHeap(arr,size):
    for i in range(size//2,-1,-1):
        heapify(arr,i,size)

def heapify(arr,index,size):
    left = 2*index + 1
    right = left +1
    max = index

    if left < size and arr[left] < arr[max]:
        max = left

    if right< size and arr[right] < arr[max]:
        max = right
    
    if index!=max:
        swap(index,max,arr)
        heapify(arr,max,size)

def swap(a,b,arr):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

arr = [10,20,40,30,80,60,50]
buildHeap(arr,7)
print(arr)
