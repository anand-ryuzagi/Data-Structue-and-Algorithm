#time complexity = O(n)
# space complexity = O(1)
import math
def rotate(arr,n,d):
    gcd = math.gcd(d,n)
    for i in range(gcd):
        temp = arr[i]
        j = i
        while True:
            k = j +d
            if k >= n:
                k = k -n
            if k==i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp


arr = [1,2,3,4,5,6]
print(f"array before rotation {arr}")
rotate(arr,6,2)
print(f"array after rotation {arr}")
