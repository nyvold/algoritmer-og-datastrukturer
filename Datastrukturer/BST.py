class Node:
    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, newNode):
        self.root = self.insert_rec(self.root, newNode)

    def insert_rec(self, root, newNode): # kjøretid O(høyden av treet) eller verste tilfelle O(n) der n er antall noder
        if root == None:
            root = newNode
            return root

        elif newNode.element < root.element:
            root.left = self.insert_rec(root.left, newNode)

        elif newNode.element > root.element:
            root.right = self.insert_rec(root.right, newNode)
        
        return root

    def search(self, node, element): #send med root når kalles
        if node == None:
            return None
        
        if node.element == element:
            return node
        
        if node.element > element:
            return self.search(node.right, element)

        if node.element < element:
            return self.search(node.left, element)

    def findMin(self, node):
        node = node.right
        while node != None:
            node = node.left
        return node

        
    