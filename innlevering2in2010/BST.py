
class Node:
    def __init__(self, newValue):
        self.value = newValue
        self.right = None
        self.left = None
    def __str__(self):
        return "'node_object'"

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, newValue):
        self.root = self.insert_recursive(self.root, newValue)
    #hjelpemetode
    def insert_recursive(self, node, newValue):
        newNode = Node(newValue)
        if node == None:
            print("kjores")
            return newNode

        elif newValue < node.value:
            node.left = self.insert_recursive(node.left, newValue)
        
        elif newValue > node.value:
            node.right = self.insert_recursive(node.right, newValue)
        return node

    def contains(self, newValue):
        return self.contains_recursive(self.root, newValue)
    
    def contains_recursive(self, node, newValue):

        if node.value == newValue:
            return True

        if newValue < node.value:
            return self.contains_recursive(node.left, newValue)
        
        elif newValue > node.value:
            return self.contains_recursive(node.right, newValue)
    
    
    
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


def main():
    bst = BST()
    bst.insert(1)
    bst.insert(2)
    bst.insert(3)

    # print(bst.contains(1))
    # print(bst.contains(2))
    # print(bst.contains(3))
    # print(bst.root.value)
    # print(bst.contains(0))
    # print(bst.contains(5))
    

main()