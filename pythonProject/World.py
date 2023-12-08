import matplotlib.pyplot as plt
import networkx as nx

# Maak een lege graaf
G = nx.Graph()
G.add_node("Brussel", pos=(665.9, 287.9))
G.add_node("Reykjavik", pos=(573.9, 217.4))
G.add_edge("Brussel", "Reykjavik", weight=2126.4)


img = plt.imread("Worldmap.png")
fig, ax = plt.subplots()
ax.imshow(img)

pos = nx.get_node_attributes(G, 'pos')
labels = nx.get_edge_attributes(G,'weight')
nx.draw(G, pos, node_size=50)
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

plt.show()