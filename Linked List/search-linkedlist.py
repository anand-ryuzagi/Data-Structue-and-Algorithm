class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
    
    def insert(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            n = self.head
            while n.next != None:
                n = n.next
            n.next = node
    
    def insertAtbegining(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def insertAt(self,index,data):
        node = Node(data)
        if index == 0:
            self.insertAtbeginning(data)
        else:
            n = self.head
            for i in range(0,index-1):
                n = n.next
            node.next = n.next
            n.next = node

    def deleteAt(self,index):
        if self.head == None:
            print("linked empty")
        else:
            n = self.head
            for i in range(0,index-1):
                n = n.next
            n.next = n.next.next

    def length(self):
        if self.head == None:
            print("linked empty")
        else:
            n= self.head
            count = 0
            while n.next != None:
                count += 1
                n = n.next
            count += 1
            return count

    def search(self,value):
        if self.head == None:
            print("linked empty")

        else:
            n = self.head
            count = self.length()
            index = 0
            for i in range(0,count):
                if n.data == value:
                    print("value found in the list",index)
                    return
                n = n.next
                index += 1
            print("value not found")

    def viewList(self):
        if self.head == None:
            print("No linkedlist created yet")

        else:
            n = self.head
            while n.next != None:
                print(n.data)
                n = n.next
            print(n.data)

