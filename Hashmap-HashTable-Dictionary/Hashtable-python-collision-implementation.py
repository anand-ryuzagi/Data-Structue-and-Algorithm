#Chaining method of collision handling in Hash Table using list under list


class Hashtable:
    def __init__(self,arraylength):
        self.max = arraylength
        self.arr = [[] for i in range(self.max)]

    def get_hash(self,key):
        h = 0 
        for i in key:
            h += ord(i) 

        return h%self.max #mod of h with length of array to map the key to a particular index

    #standard operator function
    def __setitem__(self,key,value):
        k = self.get_hash(key)
        found = False
        for index,element in enumerate(self.arr[k]):
            if len(element)==2 and element[0]==key:
                self.arr[k][index] = (key,value)
                found = True
                break
        if found == False:
            self.arr[k].append((key,value))

    def __getitem__(self,key):
        k = self.get_hash(key)
        for element in self.arr[k]:
            if element[0] == key:
                return element[1]

    def __delitem__(self,key):
        k = self.get_hash(key)
        for index,element in enumerate(self.arr[k]):
            if element[0]==key:
                del self.arr[k][index]
