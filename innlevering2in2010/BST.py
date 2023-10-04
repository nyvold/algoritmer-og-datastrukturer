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

    def visualize(self):
        self.visualize_recursive(self.root)

    def visualize_recursive(self, root):
        if not root is None:
            self.visualize_recursive(root.left)
            print(root.value)
            self.visualize_recursive(root.right)
    
    def remove(self, inpValue):
        if self.contains(inpValue) == True:
            self.root = self.remove_recursive(self.root, inpValue) 
        print(f"node med verdi: '{inpValue}' finnes ikke")

    #hjelpemetode for remove()
    def remove_recursive(self, root, inpValue):
        if root is None:
            return root

        if inpValue < root.value:
            root.left = self.remove_recursive(root.left, inpValue)
        if inpValue > root.value:
            root.right = self.remove_recursive(root.right, inpValue)
        else: #funnet noden vi skal fjerne
            if root.left is None and root.left is None:
                root = None
            elif root.right is not None:
                root.value = self.findMax_notRecursive(root)
                root.right = self.remove_recursive(root.right, root.value)
            else:
                root.value = self.findMin_notRecursive(root)
                root.left = self.remove_recursive(root.left, root.value)
    
    # hjelemetode som finner noden med minst verdi fra en gitt node, for å brukes i remove()
    def findMin(self, node):a
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
    # finner største verdi under fra gitt node 
    def findMax_notRecursive(self, node):
        max = node
        while max.right is not None:
            max = max.right
        return max.value
    
    #findMin metode som ikke er rekursiv som også funker
    def findMin_notRecursive(self, node):
        min = node
        while min.left is not None:
            min = min.left
        return min.value 

    def contains(self, newValue):
        return self.contains_recursive(self.root, newValue)
    
    #hjelpemetode til contains()
    def contains_recursive(self, node, newValue):
        if node is None:
            return False

        elif node.value == newValue:
            return True

        elif newValue < node.value:
            return self.contains_recursive(node.left, newValue)
        
        elif newValue > node.value:
            return self.contains_recursive(node.right, newValue)
    
    def size(self):
        return self.size_recursive(self.root)

    def size_recursive(self, root):
        if root is None:
            return 0
        return 1 + self.size_recursive(root.left) + self.size_recursive(root.right)

def main(): 
    bst = BST()
    output = []

    inpInt = int(sys.stdin.readline())

    for _ in range(inpInt):
        inp = sys.stdin.readline()
        stringList = inp.split()
        if len(stringList) > 1:
            stringInp = stringList[0]
            intInp = stringList[1]
            if stringInp == "insert":
                bst.insert(intInp)
            elif stringInp == "contains":
                output.append(bst.contains(intInp))
            elif stringInp == "remove":
                bst.remove(intInp)
        else:
            output.append(bst.size())
    
    print("\nOutput:")
    for out in output:
        print(out)

    f = open(f"BST_{inpInt}_test.txt", 'w')
    for line in output:
        f.write(f"{line}\n")
    f.close()
main()
