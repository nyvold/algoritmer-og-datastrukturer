
class NodeAlg:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class balansertBiSøketre:
    def convert(self, list):
        if not list:#basecase
            return []
        mid = len(list)//2
        root = NodeAlg(list[mid])
        leftSubtree = self.convert(list[mid + 1:])#rekursjon kall
        rightSubtree = self.convert(list[:mid])#rekursjon kall

        return [root.value] + leftSubtree + rightSubtree
    
    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            print(root.value, end = ' ')
            self.inOrder(root.right)

def main(): 
    bbs = balansertBiSøketre()
    listTemp = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    convertedList = bbs.convert(listTemp)
        
    print("\nInput:")
    for line in listTemp:
        print(line)
    print("\nOutput:")
    for out in convertedList:
        print(out)

main()
