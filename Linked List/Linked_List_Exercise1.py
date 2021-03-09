class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None
    

    def insert(self,data):
        node = Node(data,None)
        if self.head == None:
            self.head = node
            return

        n = self.head
        while(n.next != None):
            n = n.next
        n.next = node


    def insertAtBegin(self,data):
        node = Node(data, self.head)
        self.head = node


    def insertAtindex(self,index,data):

        if(index == 0):
            self.insertAtBegin(data)
            return
        else:
            n= self.head
            for i in range(index-1):
                n = n.next
            next = n.next
            node = Node(data,next)
            n.next = node

    def insertValues(self,data):
        for members in data:
            self.insert(members)
    
    def deleteAT(self,index):
        if(index == 0):
            self.head = self.head.next
        else:
            n = self.head
            for i in range(index-1):
                n = n.next
            n.next = n.next.next

    def getLength(self):
        count = 0
        n = self.head
        while(n):
            count += 1
            n = n.next
        return count

    def insert_after_value(self,data_after,data_to_insert):
        n = self.head
        length = self.getLength()
        for i in range(length):
            if(n.data == data_after):
                self.insertAtindex(i+1,data_to_insert)
                break
            n = n.next

    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        n = self.head
        while n.next:
            if n.next.data == data:
                n.next = n.next.next
                break
            n = n.next
    

    def show(self):
        n = self.head
        while(n.next != None):
            print(n.data)
            n = n.next
        print(n.data)

li = LinkedList()
li.insertValues(["banana","mango","grapes","orange"])
li.insert_after_value("mango","apple")
li.remove_by_value("orange")
li.remove_by_value("figs")
li.show()
