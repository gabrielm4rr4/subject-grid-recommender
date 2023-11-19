import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import numpy as np

met_comp = 'blue'
adm_gestatão = 'orange'
asp_humanos_comp = 'gold'
dev_eng_software = 'yellow'
pers_analisis_dados = 'brown'
reder_sys_computacionais = 'red'

def gerar_matriz_area_atuacao(materias):
    gerarMatriz(materias, 'area_atuacao.csv')
    plotColoredGraph(materias, areasDeAtuacaoCores(materias), 'area_atuacao.csv')

def gerar_matriz_de_prerequisitos(materias):
    gerarMatriz(materias, 'pre_requisitos.csv')
    plotColoredGraph(materias, prerrequisitosCores(materias), 'pre_requisitos.csv')

def gerarMatriz(materias, file_name = 'adj_matrix.csv'):
    # Cria uma matriz de adjacência
    matrizAdj = np.zeros((len(materias), len(materias)), dtype=int)

    # Preenche a matriz de adjacência
    for i in range(len(materias.items())):
        id, materia = list(materias.items())[i]
        for j in range(len(materias.items())):
            if i == j:
                continue

            id2, materia2 = list(materias.items())[j]
            if id in materia2['Pré-Requisitos']:
                matrizAdj[i][j] = 1

    # Create a DataFrame from the adjacency matrix
    df = pd.DataFrame(matrizAdj)

    # Write the DataFrame to a CSV file
    df.to_csv(file_name, index=False, header=False)

def areasDeAtuacaoCores(materias):
    colors = {}
    for id, materia in materias.items():
        if materia['Status'] == 'Cursada':
            colors[id] = 'grey'
            continue

        if materia['Área de atuação'] == 'Desenvolvimento e Engenharia de Software':
            colors[id] = dev_eng_software
        elif materia['Área de atuação'] == 'Administração e Gestão de Tecnologia da Informação':
            colors[id] = adm_gestatão
        elif materia['Área de atuação'] == 'Metodologias Computacionais':
            colors[id] = met_comp
        elif materia['Área de atuação'] == 'Aspectos Humanos da Computação':
            colors[id] = asp_humanos_comp
        elif materia['Área de atuação'] == 'Perspectivas e Análises de Dados':
            colors[id] = pers_analisis_dados
        elif materia['Área de atuação'] == 'Redes e Sistemas Computacionais':
            colors[id] = reder_sys_computacionais

    return colors

def prerrequisitosCores(materias):
    colors = {}
    for id, materia in materias.items():
        if materia['Tipo'] == 'Obrigatoria':
            qtd_pre_requisitos = contar_pre_requisitos(id, materias)
            if qtd_pre_requisitos == 0:
                color = '#f5b8b8'
            elif qtd_pre_requisitos > 0 and qtd_pre_requisitos < 3:
                color = '#fc7979'
            elif qtd_pre_requisitos >= 3:
                color = '#fa0505'
        elif materia['Tipo'] == 'Optativa':
            color = 'green'

        colors[id] = color

    return colors

def contar_pre_requisitos(id, materias):
    contador = 0
    for materia in materias.values():
        # Verifica se a matéria alvo é um pré-requisito para a matéria atual
        if materia['Tipo'] == 'Obrigatoria' and id in materia['Pré-Requisitos']:
            contador += 1
    return contador


def plotColoredGraph(materias, colors = {}, file_name = 'adj_matrix.csv'):
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

def gerar_ordenacao_topologica(materias):
    gerarMatriz(materias, 'ord_topologica.csv')
    topologicalOrder(materias, areasDeAtuacaoCores(materias), 'ord_topologica.csv')

def topologicalOrder(materias, colors = {}, file_name = 'adj_matrix.csv'):
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
