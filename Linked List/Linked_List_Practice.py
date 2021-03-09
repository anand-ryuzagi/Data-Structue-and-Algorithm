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

    def show(self):
        n = self.head
        while(n.next != None):
            print(n.data)
            n = n.next
        print(n.data)

li = LinkedList()
# li.insert(2)
# li.insert(3)
# li.insert(4)
# li.insertAtindex(1,67)
# li.insertAtindex(0,45)
# li.insertAtBegin(2)
# li.insertAtBegin(3)
# li.insertAtBegin(33)

li.show()
print(li.getLength())
