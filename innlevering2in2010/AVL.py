import sys
from BST import BST

class NodeAVL:
    def __init__(self, newValue):
        self.value = newValue
        self.right = None
        self.left = None
        self.height = 0
    

class AVL(BST):
    def __init__(self):
        super().__init__()

    def getHeight(self, node):
        if node is None:
            return 0
        return node.height

    def setHeight(self, node):
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    def balanceFactor(self, node):
        if node is None:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)
        
    def balance(self, node):
        if node is None:
            return node
        
        self.setHeight(node)

        if self.balanceFactor(node) > 1:
            if self.balanceFactor(node.left) < 0:
                node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if self.balanceFactor(node) < -1:
            if self.balanceFactor(node.right) > 0:
                node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        return node

    def right_rotate(self, z): 
        y = z.left
        t = y.right

        y.right = z
        z.left = t

        self.setHeight(z) 
        self.setHeight(y) 

        return y

    def left_rotate(self, z): #rett fra foil
        y = z.right
        t = y.left

        y.left = z
        z.right = t

        self.setHeight()
        self.setHeight()

        return y

    def insert(self, newValue):
        self.root = self.insert_recursive(self.root, newValue)

    #hjelpeprosedyre til insert()
    def insert_recursive(self, node, newValue):#ikke endra på fra foil
        if node is None:
            return NodeAVL(newValue)

        elif newValue < node.value:
            node.left = self.insert_recursive(node.left, newValue)
        
        elif newValue > node.value:
            node.right = self.insert_recursive(node.right, newValue)
        
        NodeAVL.setHeight(node)
        return self.balance(node)
    
    def remove(self, inpValue):
        self.root = self.remove_recursive(self.root, inpValue) #remove og remove_recursive funke ikke, sjekk forelesningfoil om bst
    
    def remove_recursive(self, node, inpValue):
        if node is None:
            return node

        if inpValue < node.value:
            node.left = self.remove_recursive(node.left, inpValue)
        elif inpValue > node.value:
            node.right = self.remove_recursive(node.right, inpValue)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
        
            temp = self.findMin_notRecursive(node.right)
            node.value = temp.value
            node.right = self.remove_recursive(node.right, temp.value)
            
            NodeAVL.setHeight(node)
        return self.balance(node)
    
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

    
def main():
    avl = AVL()
    output = []

    inpInt = int(sys.stdin.readline())

    for _ in range(inpInt):
        inp = sys.stdin.readline()
        stringList = inp.split()
        if len(stringList) > 1:
            stringInp = stringList[0]
            intInp = stringList[1]
            if stringInp == "insert":
                avl.insert(intInp)
            elif stringInp == "contains":
                output.append(avl.contains(intInp))
            elif stringInp == "remove":
                avl.remove(intInp)
        else:
            output.append(avl.size())
    
    print("\nOutput:")
    for out in output:
        print(out)

    f = open(f"AVL_{inpInt}_test.txt", 'w')
    for line in output:
        f.write(f"{line}\n")
    f.close()

main()
