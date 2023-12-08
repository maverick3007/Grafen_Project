import networkx as nx
import matplotlib.pyplot as plt

# Maak een lege graaf
G = nx.Graph()

# Voeg in één actie punten en paden toe
G.add_weighted_edges_from([("A", "B", 6.0), ("A", "C", 5.0), ("A", "D", 4.0), ("D", "F", 4.0), ("D", "E", 4.0), ("F", "E", 3.0), ("F", "G", 2.0), ("F", "H", 7.0), ("H", "G", 6.0), ("G", "B", 5.0),("G", "E", 3.0), ("B", "C", 3.0), ("B", "E", 1.0), ("C", "D", 2.0)])

# Voeg een attribuut puntwaarde toe en zet de waarde op 0 voor het startpunt en oneindig voor de andere
nx.set_node_attributes(G, float("inf"), "puntwaarde")
G.nodes["A"]["puntwaarde"] = 0
nx.set_node_attributes(G, "", "komtvan")
nx.set_node_attributes(G, False, "bezocht")

# niet bezochte buren van A
def padzoeker(start):
    startpunt = G.nodes[start]
    buren = G.neighbors(start)
    starpuntwaarde = startpunt["puntwaarde"]
    startpunt["bezocht"] = True
    volgendpunt = "GEEN"
    minimum = float("inf")

    print("Dijkstra pad:")
    for buur in buren:
        test = buur
        padwaarde = G.get_edge_data(start, buur)["weight"]
        huidige_puntwaarde = G.nodes[buur]['puntwaarde']
        puntwaarde = starpuntwaarde + padwaarde
        if G.nodes[buur]['bezocht'] == False:
            if puntwaarde < G.nodes[buur]['puntwaarde']:
                G.nodes[buur]['puntwaarde'] = starpuntwaarde + padwaarde
                G.nodes[buur]['komtvan'] = start
            if G.nodes[buur]['puntwaarde'] < minimum:
                minimum = G.nodes[buur]['puntwaarde']
                volgendpunt = buur
    if volgendpunt != "GEEN":
        G.nodes[volgendpunt]["komtvan"] = start
        print(volgendpunt)
        padzoeker(volgendpunt)

    print("Kortste pad:")
    pad = []
    destnode = "H"
    finished = False
    while not finished:
        pad.insert(0, destnode)
        previousNode = G.nodes[destnode]["komtvan"]

        if previousNode != "":
            destnode = previousNode
        else:
            finished = True
    return pad



padzoeker("A")

for node in G.nodes:
    print(node)

labels = nx.get_edge_attributes(G,'weight')
pos=nx.spring_layout(G, seed=5)
nx.draw(G, pos, with_labels=True)
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)



plt.show()