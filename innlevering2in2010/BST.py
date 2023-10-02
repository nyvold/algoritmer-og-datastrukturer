import sys

class Node: #node klasse som inneholder verdi og "barnenodene"
    def __init__(self, newValue):
        self.value = newValue
        self.right = None
        self.left = None

    def __str__(self):#magisk tostring metode for å hjelpe med debugging
        return "'node_object'"

class BST:#binary search tree, binert søke tre klassen
    def __init__(self):#rot starter som none
        self.root = None
    
    def insert(self, newValue):
        self.root = self.insert_recursive(self.root, newValue)

    #hjelpeprosedyre til insert()
    def insert_recursive(self, node, newValue):
        if node is None:
            return Node(newValue)

        elif newValue < node.value:
            node.left = self.insert_recursive(node.left, newValue)
        
        elif newValue > node.value:
            node.right = self.insert_recursive(node.right, newValue)
        
        return node
    
    def remove(self, inpValue):
        self.root = self.remove_recursive(self.root, inpValue) #remove og remove_recursive funke ikke, sjekk forelesningfoil om bst
    
    #hjelpemetode for remove()
    def remove_recursive(self, node, inpValue):
        if node is None:
            return node

        if inpValue < node.value:
            node.left = self.remove_recursive(node.left, inpValue)
            # return node
        if inpValue > node.value:
            node.right = self.remove_recursive(node.right, inpValue)
            # return node
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
        
            temp = self.findMin_notRecursive(node.right)
            node.value = temp.value
            node.right = self.remove_recursive(node.right, temp.value)

        return node
    
    # hjelemetode som finner noden med minst verdi fra en gitt node, for å brukes i remove()
    def findMin(self, node):
        return self.findMin_recursive(node)
    
    #hjelpemetode til hjelpemetoden findMin()
    def findMin_recursive(self, node):
        min = node
        if min is None:
            print("input for 'findMin()' is None")
            return
        if min.left is None:
            return min
        return self.findMin_recursive(min.left)

    #findMin metode som ikke er rekursiv som også funker
    def findMin_notRecursive(self, node):
        min = node
        while min.left is not None:
            min = min.left
        return min 

    def contains(self, newValue):
        return self.contains_recursive(self.root, newValue)
    
    #hjelpemetode til contains()
    def contains_recursive(self, node, newValue):
        if node is None:
            return False

        if node.value == newValue:
            return True

        if newValue < node.value:
            return self.contains_recursive(node.left, newValue)
        
        elif newValue > node.value:
            return self.contains_recursive(node.right, newValue)
    
    def size(self):
        return self.size_recursive(self.root)

    def size_recursive(self, root):
        if root is None:
            return 0
        return 1 + self.size_recursive(root.left) + self.size_recursive(root.right)

    #eksempel input:
    # 9
    # insert 1  
    # insert 2  
    # insert 3  
    # insert 1  
    # contains 1 
    # contains 0
    # remove 1
    # contains 1
    # size
    # output:
    # true
    # false 
    # false 
    # 2
def main(): #fiks input fra terminal
    bst = BST()
    output = []
    bst.insert(1)
    bst.insert(2)
    bst.insert(3)
    bst.insert(1)
    print(bst.contains(1))
    print(bst.contains(0))
    bst.remove(1)
    print(bst.contains(1))
    print(bst.size())
    # inpInt = int(sys.stdin.readline())
    # output = []

    # for _ in range(inpInt):
    #     inp = sys.stdin.readline()
    #     print(inp)
    #     if inp != "size":
    #         stringList = inp.split()
    #         stringInp = stringList[0]
    #         intInp = int(stringList[1])
    #     else:
    #         output.append(bst.size())

    #     if stringInp == "insert":
    #         bst.insert(intInp)
    #     elif stringInp == "contains":
    #         output.append(bst.contains(intInp))
    #     elif stringInp == "remove":
    #         bst.remove(intInp)
            

    # for out in output:
    #     print(out)
main()
