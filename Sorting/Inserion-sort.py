# Insertion sort : in this a value is picked and is compared with the value of it previous indexes and if the value at index-1 is greater than the value at index then the values are swapped and it continues to all prvious indexes until the right position of that value is reached. Example: arranging a deck of card.

#Time complexity: O(n^2)
#space complexity: O(n)

def insertionSort(arr,size):
    for i in range(1,size):
        value = arr[i]
        index = i
        while (index > 0 and arr[index-1] > value):
            arr[index] = arr[index-1]
            index -= 1
        arr[index] = value



arr = [5,2,1,4,9,6,8,7,3]
print("Array before sort: ",arr)
insertionSort(arr,len(arr))
print("Array after sort: ",arr)
