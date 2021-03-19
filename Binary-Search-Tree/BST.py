#BinarySearchTree algorithm

class BinarySearchTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_node(self,value):
        if value == self.data:
            return
        
        if value < self.data:
            if self.left:
                self.left.add_node(value)
            else:
                self.left = BinarySearchTree(value)
        else:
            if self.right:
                self.right.add_node(value)
            else:
                self.right = BinarySearchTree(value)
    
    def inOrderTravers(self):
        elements = []
        if self.left:
            elements += self.left.inOrderTravers()
        
        elements.append(self.data)

        if self.right:
            elements += self.right.inOrderTravers()

        return elements

    def search(self,value):
        if self.data == value:
            return True
        if self.left:
            return self.left.search(value)
        else:
            return False
        
        if self.right:
            return self.right.search(value)
        else:
            return False

    def find_max(self):
        if self.right == None:
            return self.data
        else:
            return self.right.find_max()

    def find_min(self):
        if self.left == None:
            return self.data
        else:
            return self.left.find_min()


def buildTree(elements):
    root = BinarySearchTree(elements[0])

    for i in range(1,len(elements)):
        root.add_node(elements[i])

    return root

if __name__ == '__main__':
    arr = [10,9,5,6,80]
    onetree = buildTree(arr)
    print(onetree.inOrderTravers())
    print(onetree.search(11))
