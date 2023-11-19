import numpy as np
import pandas as pd

from . import cores
from . import grafo_colorido
from . import ordem_topologica

def gerar_matriz_area_atuacao(materias):
    gerarMatriz(materias, 'area_atuacao.csv')
    grafo_colorido.gerar(materias, cores.areas_de_atuacao(materias), 'area_atuacao.csv')

def gerar_matriz_de_prerequisitos(materias):
    gerarMatriz(materias, 'pre_requisitos.csv')
    grafo_colorido.gerar(materias, cores.pre_requisitos(materias), 'pre_requisitos.csv')

def gerar_ordenacao_topologica(materias):
    gerarMatriz(materias, 'ord_topologica.csv')
    ordem_topologica.gerar(materias, {}, 'ord_topologica.csv')

def gerarMatriz(materias, file_name):
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

