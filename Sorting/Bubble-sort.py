# Bubble sort : It is like a air bubble in the water in which the larger bubble rises first and the smaller one will follow it and as the largest bubble reaches the end it pop out.

# Algorithm
# the outer loop iterate equal to the number of elements in the array
# at each iteration of outer loop, a inner loop is initiated from index =0 to size-1-i(-i to exclude the last sorted element in the next iteration)
# in inner loop continuously adjacent values are compared and if there is the first value is larger than second then the values are swapped


def selectionSort(arr,size):
    flag = False
    for i in range(size-1):
        for j in range(size-1-i):
            if(arr[j]>arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                flag = True
    
        if flag == False:
            break


arr = [1,2,3,4,5,7,6]
print("Array before sort: ",arr)
selectionSort(arr,len(arr))
print("Array after sort: ",arr)
