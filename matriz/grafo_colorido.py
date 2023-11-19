import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def gerar(materias, colors = {}, file_name = 'adj_matrix.csv'):
    adjacency_matrix = pd.read_csv(file_name, header=None).values
    G = nx.DiGraph(adjacency_matrix)

    # Use Fruchterman-Reingold layout to minimize edge crossings
    pos = nx.fruchterman_reingold_layout(G, k=10, iterations=1000, scale=10)

    color_per_node = [colors.get(node, 'skyblue') for node in G.nodes()]

    plt.figure(figsize=(15,15))
    labels = []
    for id, materia in materias.items():
        labels.append(str(id))

    node_labels = {node: labels[node] for node in G.nodes()}
    # Visualize the graph
    nx.draw(G, pos, with_labels=True, labels=node_labels, font_weight='bold', node_size=700, node_color=color_per_node, font_size=10, font_color='black', edge_color='gray', linewidths=1, alpha=0.7)

    # Show the plot
    plt.show()

