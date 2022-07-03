# EXERCISE 12.2
# -----------------------------------------------
print('Exercise 12.2')
print('------------')

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
for node in (1,2,3,4,5):
    G.add_node(node)

for (a,b) in [(1,2),(2,4),(2,3),(3,4),(4,5)]:
    G.add_edge(a,b)

nx.draw(G,with_labels=True)
plt.savefig('Graph.jpg')
print('Graph with 5 nodes and 5 edges saved to Graph.jpg')
