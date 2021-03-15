# Algorithm Linear Probing Hashing
# 1. Initialize the hashtable with -1
# 2.Find the key with data % size of
# 4. if hashtable[key] is available i,e -1 then insert the data 
# 5. Else there is collision, so increment the key value by 1 continously using key = key+1 % size until find the next available space.
# 6.If any index is available insert the data.
# 7. If in this iteration we again reach the starting point, we can understand that no space is n available. 

class HashTable():
    def __init__(self,arr_size):
        self.arr_size = arr_size
        self.arr = [-1 for i in range(self.arr_size)]
       

    def hash_key(self,key):
        return key % self.arr_size

    def insert(self,value): #insert with linear probing
        key= self.hash_key(value)
        index = key

        while self.arr[index] != -1:
            index = (index+1)% self.arr_size
            if index == key:
                print("Hashtable full")
                return 0
            
        self.arr[index] = value
        print(f"value added at index: {index}")

    def remove(self,value): #remove  with linear probing implementation
        key = self.hash_key(value)
        index = key

        while self.arr[index] != value:
            index = (index+1)%self.arr_size

            if index == key:
                print("Value Not found")
                return 0

        self.arr[index] = -1
        print(f"value removed at {index}")

    def search(self,value): #search with linear probing implementation
        key = self.hash_key(value)
        index = key

        while self.arr[index] != value:
            index = (index+1)%self.arr_size
            if index == key:
                print("Value Not Found")
                return 0
        print(f"value found at {index}")
