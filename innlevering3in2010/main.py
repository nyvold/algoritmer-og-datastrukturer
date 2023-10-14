import sys
from Graph import Graph


def main():
        #oppgave 1
        g = Graph("movies", "actors")

        num_nodes = len(g.v)
        num_edges = sum(len(adj_list) for adj_list in g.e.values()) // 2
        
        
        actor1 = "nm2255973"
        actor2 = "nm8076281"
        actor3 = "nm0000288"
        actor4 = "nm0424060"
        actor5 = "nm0000460"

        #oppgave 2
        output = []
        for i in g.bfs_shortest_path_between(actor1, actor2):
            if i[:2] == "nm":
                name = g.actors[i]["name"]
                output.append(f"{name}\n    v")
            else:
                title = g.movies[i]["title"]
                rating = g.movies[i]["rating"]
                output.append(f"[ {title} ({rating}) ]\n    v")
        
        #oppgave 3
        inpDijkstra = g.dijkstra(actor4, actor2)
        dijkstra_path = inpDijkstra[0]
        dijkstra_weight = inpDijkstra[1]
        output_dijkstra = []
        for i in dijkstra_path:
            if i[:2] == "nm":
                name = g.actors[i]["name"]
                output_dijkstra.append(f"{name}\n    v")
            else:
                title = g.movies[i]["title"]
                rating = g.movies[i]["rating"]
                output_dijkstra.append(f"[ {title} ({rating}) ]\n    v")
        output_dijkstra.append(f"Path weight: {dijkstra_weight}")

        
        #output oppgaver
        #oppgave1
        print(f"nodes: {num_nodes}")
        print(f"edges: {num_edges}")
        print("\n")
        #oppgave2
        print(f"shortest path from {actor1} to {actor2}:")
        for i in output:
            print(i)
        print("\n")
        #oppgave3
        print(f"shortest path from {actor1} to {actor2} with weight:")
        for i in output_dijkstra:
            print(i)

        
if __name__ == '__main__':
    main()
