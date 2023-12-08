Urettet_graf
oppgave 11 eksamen h18

idee:
gjør en dfs traversering

IsTree(G)
V, E <- tom liste
visited <-  tom liste
for node in V do:
    if node not in visited then:
        ingenSykler <- dfsVisit(G, node, visited)
for node in visited do:
    if node not in V then:
        sammenhengende <- false
return ingenSykler and sammenhengende


dfsVisit(G, node, visited)
legg til node i visited
for (node, nabo) in E do:
    if nabo not in visited then:
        dfsVisit(G, nabo, visited)
    else:
        return false
return true