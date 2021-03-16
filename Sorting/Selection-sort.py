# Selection sort : Select a position and compare all the values for its best suitable value

# Algorithm:
# select a index i
# compare all the values with value at index i by iterating from i+1 to length of array
# if the comparing value satisfies the arr[i]>arr[j] condition then swap the values
# repeat all above until the values sorted correctly.

def selectionSort(arr,size):
    for i in range(size):
        for j in range(i+1,size):
            if(arr[i]>arr[j]):
                temp =arr[i]
                arr[i] = arr[j]
                arr[j] = temp



arr = [2,1,4,9,6,8]
print("Array before sort: ",arr)
selectionSort(arr,len(arr))
print("Array after sort: ",arr)
