import sys
def kattunge():
    d = {}
    # d2 = {25:[24], 4:[3, 1, 2], 13:[9, 4, 11], 10:[20, 8, 7], 32:[10,21], 23:[13,19,32,22], 19:[12,5,14,17,30], 14:[6,15,16], 30:[18,31,29], 24:[23,26], 26:[27,28]}
    temp = False
    root = None
    for line in sys.stdin:
        if temp == False:
            root = line
            temp = True
        stringList = line.split()
        if len(stringList) > 1:
            key = stringList[0]
            values = []
            for i in stringList:
                values.append(i)
            d[key] = values
        else:
            break

    # inp = input()
    # for _ in range(int(inp)):
    #     intinp = input()
    #     if intinp == "-1":
    #         break
    #     sl = intinp.split()
    #     if len(sl) == 1:
    #         temp = sl[0]
    #     else:
    #         key = sl[0]
    #         values = sl[1:]
    #         d[key] = values
    print(d)
    p = [] #p for path
    t = '14' #t for temp variabel
    p.append(root)
    while not root in p:
        for k, v in d.items():
            if len(v) == 1:
                root = k
            for s in v:
                if s == t:
                    t = k
                    p.append(t)
    print(f"path: {p}")
    # print(d)

def main():
    kattunge()
main()

# for line in sys.stdin:
#         stringList = line.split()
#         if len(stringList) > 1:
#             command = stringList[0]
#             inp = int(stringList[1])
#             if command == "insert":
#                 sc.insert(inp)
#             elif command == "contains":
#                 output.append(sc.contains(inp))
#             elif command == "remove":
#                 sc.remove(inp)
#         else:
#             output.append(sc.size())
#         if line == "\n":
#             break
    
#     print("\nOutput:")
#     for out in output:
#         print(out)
