import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def gerar(materias, colors = {}, file_name = 'adj_matrix.csv'):
    adjacency_matrix = pd.read_csv(file_name, header=None).values
    G = nx.DiGraph(adjacency_matrix)
    color_per_node = [colors.get(node, 'skyblue') for node in G.nodes()]

    pos = {node:(node,0) for node in G.nodes()}
    labels = []
    for id, materia in materias.items():
        labels.append(str(id))

    node_labels = {node: labels[node] for node in G.nodes()}

    plt.figure(figsize=(15,5))

    ax = plt.gca()
    for edge in G.edges():
        source, target = edge
        rad = 0.8
        rad = rad if source%2 else -rad
        ax.annotate("", xy=pos[source], xytext=pos[target], arrowprops=dict(arrowstyle="<-,head_length=0.6,head_width=0.4", color="black", connectionstyle=f"arc3,rad={rad}", alpha=0.6, linewidth=1.5)) 

    nx.draw_networkx_nodes(G, pos=pos, node_size=500, node_color='skyblue', alpha=0.7)
    nx.draw_networkx_labels(G, pos=pos, labels=node_labels, font_color='black')

    plt.box(False)
    plt.show()
