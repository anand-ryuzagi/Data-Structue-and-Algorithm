class Hashtable:
    def __init__(self,arraylength):
        self.max = arraylength
        self.arr = [None for i in range(self.max)]

    def get_hash(self,key):
        h = 0 
        for i in key:
            h += ord(i) 

        return h%self.max #mod of h with length of array to map the key to a particular index

    def add(self,key,value):
        k = self.get_hash(key)
        self.arr[k] = value

    def get(self,key):
        k = self.get_hash(key)
        return self.arr[k]

    #standard operator function
    def __setitem__(self,key,value):
        k = self.get_hash(key)
        self.arr[k] = value  

    def __getitem__(self,key):
        k = self.get_hash(key)
        return self.arr[k] 

    def __delitem__(self,key):
        k = self.get_hash(key)
        self.arr[k] = None
        
