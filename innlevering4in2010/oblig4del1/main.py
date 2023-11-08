from hashTableSC import hashTableSC
from BST import BST, Node
import sys
import time

def main():
    # lp = linearprobingMap()
    
    # separate chaining og binært søketre
    bst = BST()
    sc = hashTableSC()

    inputTest = [] 

    inp = input()
    fileContent = open(inp).readlines()
    for line in fileContent:
        inputTest.append(line)

    # --------bst test----------

    bst_output = []

    bst_start = time.time()

    for command in fileContent:
        stringList = command.split()
        if len(stringList) > 1:
            stringInp = stringList[0]
            intInp = int(stringList[1])
            if stringInp == "insert":
                bst.insert(intInp)
            elif stringInp == "contains":
                bst_output.append(bst.contains(intInp))
            elif stringInp == "remove":
                bst.remove(intInp)
        else:
            bst_output.append(bst.size())

    bst_end = time.time()

    print("\n\n-----bst result-----")
    print(f"bst runtime: {bst_end - bst_start}")
    # print("bst output: ")
    # for out in bst_output:
    #     print(out)
    
    # --------hashtable test----------

    sc_output = []

    sc_start = time.time()

    for command in fileContent:
        stringList = command.split()
        if len(stringList) > 1:
            stringInp = stringList[0]
            intInp = int(stringList[1])
            if stringInp == "insert":
                sc.insert(intInp)
            elif stringInp == "contains":
                sc_output.append(sc.contains(intInp))
            elif stringInp == "remove":
                sc.remove(intInp)
        else:
            sc_output.append(sc.size())
    
    sc_end = time.time()

    print("\n\n-----hashtable result-----")
    print(f"hashtable runtime: {sc_end - sc_start}")
    print("\n\n")
    # print("hashtable output: ")
    # for out in sc_output:
    #     print(out)

    # inputs/input_10.txt
    # inputs/input_100.txt
    # inputs/input_1000.txt
    # inputs/input_10000.txt

if __name__ == '__main__':
    main()