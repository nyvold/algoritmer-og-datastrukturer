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

# ------------------------------------------------------
    # inputs/input_10.txt
#     -----bst result-----
# bst runtime: 6.604194641113281e-05


# -----hashtable result-----
# hashtable runtime: 3.5762786865234375e-05
# ------------------------------------------------------



# ------------------------------------------------------
    # inputs/input_100.txt
#     -----bst result-----
# bst runtime: 0.0003838539123535156


# -----hashtable result-----
# hashtable runtime: 0.00016999244689941406
# ------------------------------------------------------


# ------------------------------------------------------
    # inputs/input_1000.txt
#     -----bst result-----
# bst runtime: 0.0073089599609375


# -----hashtable result-----
# hashtable runtime: 0.0016109943389892578
# ------------------------------------------------------



# ------------------------------------------------------
    # inputs/input_10000.txt:
#     -----bst result-----
# bst runtime: 0.44661402702331543


# -----hashtable result-----
# hashtable runtime: 0.08738994598388672
# ------------------------------------------------------


if __name__ == '__main__':
    main()