Whops!-logger
eksamen h21

ideen:
topologisk sortere alle v i V til en stack. Gå gjennom stacken og sortere den. selv om verste tilfelle for sorteringen er n^2 så vil sorteringen gå fort fordi den får stacken som nesten er sortert, sorteringen bare finpusser siste output.

dfsTopSort(G):
V, E <- G
stack <- tom liste
visited <- tom liste
for node in V do:       //DFStopsorter grafen til en ca. sortert liste
    if node not in visited then:
        dfsVisit(G, node, visited, stack)

for i ← 1 to stack.length - 1 do  //bruker insertion sort for å sortere, mener den er best egnet for casen
    j ← i
        while j > 0 and stack[j-1] > stack[j] do
            stack[j-1], stack[j] <- stackA[j], stack[j-1]
            j ← j − 1
for node in stack do
    print(node)

dfsVisit(G, node, visited, stack):
legg til node i visited
for (node, u) in E do:
    if u not in visited then:
        dfsVisit(G, u, visited, stack)
stack.push(node)
