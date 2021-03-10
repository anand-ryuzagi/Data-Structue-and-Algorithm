class TreeNode: #creating a base node class
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None
    
    def addChild(self,child): #function to add child
        child.parent = self     #this will set child.parent to self i,e current instance to parent of this child added  
        self.children.append(child)

    def get_level(self): #getting level of each node
        level = 0 #when there is no parent level will be zero
        p = self.parent
        while p: #checking if self.parent has some value then while loop continue
            level += 1
            p = p.parent
        return level

    def print_tree(self): #beautifying the print tree
        space = " "* self.get_level()
        if self.parent: 
            prefix = space + "|--"
        else:
            prefix = space + ""
        print(prefix+self.data)
        if len(self.children) > 0: #condition to check it has children or not
            for child in self.children:
                child.print_tree() #recursion to get child of child

def buildTree():
    root = TreeNode("Electronics")

    laptop = TreeNode("laptop")
    laptop.addChild(TreeNode("acer"))
    laptop.addChild(TreeNode("Lenovo"))
    laptop.addChild(TreeNode("Dell"))

    tv = TreeNode("Tv")
    tv.addChild(TreeNode("Sony"))
    tv.addChild(TreeNode("Samsung"))
    tv.addChild(TreeNode("LG"))

    mobile = TreeNode("Mobile")
    mobile.addChild(TreeNode("Samsung"))
    mobile.addChild(TreeNode("Iphone"))
    mobile.addChild(TreeNode("Nokia"))

    root.addChild(laptop)
    root.addChild(tv)
    root.addChild(mobile)

    return root

if __name__ == "__main__":
    root = buildTree()
    root.print_tree()
