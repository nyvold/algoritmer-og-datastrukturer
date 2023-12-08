
ideen:
gjør DFS på treet, underveis sjekke om noder er inrange i gitt interval. 
hvis node er i dette intervallet, sette noden på riktig plass i inrange listen. 
grunnen til at jeg vil gjøre det slik er at underveis kan jeg gjøre noe på n tid istedenfor 
å måtte sortere inrange listen på slutten som kan potensielt ta lengere tid. 

def DFS(B, a, b):
    V, E = B
    inrange = []
    visited = []
    for node in V do:
        if not node in visited then:
            DFSvisit(B, node, visited, inrange)


def DFSvisit(B, node, visited, inrange, a, b):
    visited.append(noe)
    if node.element < b and node.element > a then:
        if inrange.length == 0 then:
            inrange.append(node)
        else then:
            for i in range(inrange.length) do:
                if inrange[i].element < node.element then:
                    if inrange[i+1] != null then:
                        indeks = i
                        for i in range(inrange.length, inrange[i+1], -1) do:
                            inrange[i+1] = inrange[i]                              
                        inrange[indeks] = node 
                    else then:                                         
                        inrange.append(node)
    for child in node.childen do:
        if not child in visited then:
            DFSVisit(B, child, visited, inrange, a, b)

eller
