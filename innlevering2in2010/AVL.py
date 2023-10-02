import sys
from BST import BST

class NodeAVL:
    def __init__(self, newValue):
        self.value = newValue
        self.right = None
        self.left = None
        self.height = 1
    

class AVL(BST):
    def __init__(self):
        super().__init__()

    def getHeight(self, node):
        if not node:
            return 0
        return node.height

    def setHeight(self, node):
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    def balanceFactor(self, node):
        if not node:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)
        
    def balance_afterInsert(self, node, newValue):
        if not node:
            return node
        
        # self.setHeight(node)
        bf = self.balanceFactor(node)

        if bf > 1:
            if newValue < node.left.value:
                return self.right_rotate(node)
            else:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)
        
        if bf < -1:
            if newValue > node.right.value:
                return self.left_rotate(node)
            else:
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)
            
        return node
    
    def balance_afterRemove(self, node):
        # self.setHeight(node)
        bf = self.balanceFactor(node)

        if bf > 1:
            if self.balanceFactor(node.left) >= 0:
                return self.right_rotate(node)
            else:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)
        
        if bf < -1:
            if self.balanceFactor(node.right) <= 0:
                return self.left_rotate(node)
            else:
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
        if not node:
            return NodeAVL(newValue)

        elif newValue < node.value:
            node.left = self.insert_recursive(node.left, newValue)
        
        else:
            node.right = self.insert_recursive(node.right, newValue)
        
        self.setHeight(node)
        return self.balance_afterInsert(node, newValue)
    
    def delete(self, node, inpValue):
        if not node:
            return node

        if inpValue < node.value:
            node.left = self.delete(node.left, inpValue)
        elif inpValue > node.value:
            node.right = self.delete(node.right, inpValue)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
        
            temp = self.findMin_alt(node.right)#prøv begge findmn metoder
            node.value = temp.value
            node.right = self.remove_recursive(node.right, temp.value)
        
        if node is None:
            return node
        
        self.setHeight(node)
        return self.balance_afterRemove(node)

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
                temp = node.right
                node = None
                return temp
            if node.right is None:
                temp = node.left
                node = None
                return temp
        
            temp = self.findMin_alt(node.right)#prøv begge findmn metoder
            node.value = temp.value
            node.right = self.remove_recursive(node.right, temp.value)
            
        self.setHeight(node)
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
    
    def finMin_alt(self, node):
        if node is None or node.left is None:
            return node
        return self.findMin_Alt(node.left)

    
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
                avl.delete(intInp)
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
