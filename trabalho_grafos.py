import json
import random
import semester
import subject

HORAS_OPTATIVAS = 672
horas_optativas_registradas = 0

# Função que percorre o grafo e define as matérias já cursadas
def define_materias_cursadas(materias_cursadas = {}):
    # Colore o grafo inicial com todas matérias com status "Pendente" e define como "Cursadas" caso esteja na lista de "materias_cursadas" dada no input do aluno
    grafoCCO = {
        0: {'Nome': 'Fundamentos de Programação', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [], 'Semestre': 1, "Crédito": 64},
        1: {'Nome': 'Programação Orientada a Objetos', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [0], 'Semestre': 3, "Crédito": 64},
        2: {'Nome': 'Programação Web', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [1], 'Semestre': 4, "Crédito": 64},
        3: {'Nome': 'Engenharia de Software I', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [], 'Semestre': 3, "Crédito": 64},
        4: {'Nome': 'Programação Lógica e Funcional', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [21], 'Semestre': 2, "Crédito": 64},
        5: {'Nome': 'Banco de Dados I', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [14], 'Semestre': 5, "Crédito": 64},
        6: {'Nome': 'Inteligência Artificial', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [22], 'Semestre': 5, "Crédito": 64},
        7: {'Nome': 'Introdução à Computação Visual', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [22, 1], 'Semestre': 5, "Crédito": 64},
        8: {'Nome': 'Redes de Computadores', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [9], 'Semestre': 4, "Crédito": 64},
        9: {'Nome': 'Sistemas Operacionais', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [13, 11], 'Semestre': 3, "Crédito": 64},
        10: {'Nome': 'Arquitetura de Computadores I', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [], 'Semestre': 1, "Crédito": 64},
        11: {'Nome': 'Arquitetura de Computadores II', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [10], 'Semestre': 2, "Crédito": 64},
        12: {'Nome': 'Sistemas Embarcados', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [13, 11], 'Semestre': 4, "Crédito": 64},
        13: {'Nome': 'Algoritmos e Estruturas de Dados I', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [0], 'Semestre': 2, "Crédito": 64},
        14: {'Nome': 'Algoritmos e Estruturas de Dados II', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [13], 'Semestre': 3, "Crédito": 64},
        15: {'Nome': 'Análise e Projeto Orientados a Objeto', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [1], 'Semestre': 5, "Crédito": 64},
        16: {'Nome': 'Projeto e Análise de Algoritmos', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [14, 21, 23], 'Semestre': 4, "Crédito": 64},
        17: {'Nome': 'Teoria da Computação', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [4, 16], 'Semestre': 5, "Crédito": 64},
        18: {'Nome': 'Compiladores', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [17], 'Semestre': 6, "Crédito": 64},
        19: {'Nome': 'Cálculo A', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [], 'Semestre': 1, "Crédito": 64},
        20: {'Nome': 'Cálculo B', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [19], 'Semestre': 2, "Crédito": 64},
        21: {'Nome': 'Matemática Discreta', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [], 'Semestre': 1, "Crédito": 64},
        22: {'Nome': 'Métodos Matemáticos para Análise de Dados', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [19, 13, 21], 'Semestre': 3, "Crédito": 64},
        23: {'Nome': 'Algoritmos em Grafos', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [13], 'Semestre': 3, "Crédito": 64},
        24: {'Nome': 'Modelagem Computacional', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [19], 'Semestre': 2, "Crédito": 64},
        25: {'Nome': 'Cálculo Numérico para Computação', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [19], 'Semestre': 4, "Crédito": 64},
        26: {'Nome': 'Computação e Sociedade', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [], 'Semestre': 7, "Crédito": 64},
        27: {'Nome': 'Interação Humano-Computador', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [2], 'Semestre': 6, "Crédito": 64},
        28: {'Nome': 'Metodologia Científica', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [], 'Co-Requisitos': [71], 'Semestre': 7, "Crédito": 64},
        29: {'Nome': 'Projeto Integrado', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [], 'Semestre': 1, "Crédito": 32},
        30: {'Nome': 'Arquitetura de Software', 'Status': 'Pendente', 'Área de atuação': 'Desenvolvimento e Engenharia de Software', 'Tipo': 'Optativa', 'Pré-Requisitos': [3], "Crédito": 64},
        31: {'Nome': 'Padrões de Projeto', 'Status': 'Pendente', 'Área de atuação': 'Desenvolvimento e Engenharia de Software', 'Tipo': 'Optativa', 'Pré-Requisitos': [3, 2], "Crédito": 64},
        32: {'Nome': 'Engenharia de Software Experimental', 'Status': 'Pendente', 'Área de atuação': 'Desenvolvimento e Engenharia de Software', 'Tipo': 'Optativa', 'Pré-Requisitos': [3], "Crédito": 64},
        33: {'Nome': 'Tópicos em DES I', 'Status': 'Pendente', 'Área de atuação': 'Desenvolvimento e Engenharia de Software', 'Tipo': 'Optativa', 'Pré-Requisitos': [3], "Crédito": 64},
        34: {'Nome': 'Tópicos em DES II', 'Status': 'Pendente', 'Área de atuação': 'Desenvolvimento e Engenharia de Software', 'Tipo': 'Optativa', 'Pré-Requisitos': [3], "Crédito": 64},
        35: {'Nome': 'Desenvolvimento de Jogos', 'Status': 'Pendente', 'Área de atuação': 'Desenvolvimento e Engenharia de Software', 'Tipo': 'Optativa', 'Pré-Requisitos': [0], "Crédito": 64},
        36: {'Nome': 'Desenvolvimento para Dispositivos Móveis', 'Status': 'Pendente', 'Área de atuação': 'Desenvolvimento e Engenharia de Software', 'Tipo': 'Optativa', 'Pré-Requisitos': [2], "Crédito": 64},
        37: {'Nome': 'Reutilização de Software', 'Status': 'Pendente', 'Área de atuação': 'Desenvolvimento e Engenharia de Software', 'Tipo': 'Optativa', 'Pré-Requisitos': [38, 1, 31], "Crédito": 64},
        38: {'Nome': 'Engenharia de Software II', 'Status': 'Pendente', 'Área de atuação': 'Desenvolvimento e Engenharia de Software', 'Tipo': 'Optativa', 'Pré-Requisitos': [3], "Crédito": 64},
        39: {'Nome': 'Gerência de projetos de software', 'Status': 'Pendente', 'Área de atuação': 'Desenvolvimento e Engenharia de Software', 'Tipo': 'Optativa', 'Pré-Requisitos': [38], "Crédito": 64},
        40: {'Nome': 'Desenvolvimento de sistemas web', 'Status': 'Pendente', 'Área de atuação': 'Desenvolvimento e Engenharia de Software', 'Tipo': 'Optativa', 'Pré-Requisitos': [3, 5, 2], "Crédito": 64},
        41: {'Nome': 'Maratona de programação I', 'Status': 'Pendente', 'Área de atuação': 'Desenvolvimento e Engenharia de Software', 'Tipo': 'Optativa', 'Pré-Requisitos': [13], "Crédito": 48},
        42: {'Nome': 'Maratona de programação II', 'Status': 'Pendente', 'Área de atuação': 'Desenvolvimento e Engenharia de Software', 'Tipo': 'Optativa', 'Pré-Requisitos': [41], "Crédito": 48},
        43: {'Nome': 'Banco de Dados II', 'Status': 'Pendente', 'Área de atuação': 'Persistência e Análise Dados', 'Tipo': 'Optativa', 'Pré-Requisitos': [5], "Crédito": 64},
        44: {'Nome': 'Introdução à Análise de Dados', 'Status': 'Pendente', 'Área de atuação': 'Persistência e Análise Dados', 'Tipo': 'Optativa', 'Pré-Requisitos': [22], "Crédito": 64},
        45: {'Nome': 'Banco de Dados noSQL', 'Status': 'Pendente', 'Área de atuação': 'Persistência e Análise Dados', 'Tipo': 'Optativa', 'Pré-Requisitos': [5], "Crédito": 64},
        46: {'Nome': 'Tópicos em PAD', 'Status': 'Pendente', 'Área de atuação': 'Persistência e Análise Dados', 'Tipo': 'Optativa', 'Pré-Requisitos': [5, 44], "Crédito": 64},
        47: {'Nome': 'Modelagem Geométrica e Visual', 'Status': 'Pendente', 'Área de atuação': 'Metodologias Computacionais e Otimização', 'Tipo': 'Optativa', 'Pré-Requisitos': [22, 7], "Crédito": 64},
        48: {'Nome': 'Visão Computacional', 'Status': 'Pendente', 'Área de atuação': 'Metodologias Computacionais e Otimização', 'Tipo': 'Optativa', 'Pré-Requisitos': [21, 7], "Crédito": 64},
        49: {'Nome': 'Métodos Exatos', 'Status': 'Pendente', 'Área de atuação': 'Metodologias Computacionais e Otimização', 'Tipo': 'Optativa', 'Pré-Requisitos': [22], "Crédito": 64},
        50: {'Nome': 'Metaheurísticas', 'Status': 'Pendente', 'Área de atuação': 'Metodologias Computacionais e Otimização', 'Tipo': 'Optativa', 'Pré-Requisitos': [22], "Crédito": 64},
        51: {'Nome': 'Tópicos em MCO', 'Status': 'Pendente', 'Área de atuação': 'Metodologias Computacionais e Otimização', 'Tipo': 'Optativa', 'Pré-Requisitos': [22], "Crédito": 64},
        52: {'Nome': 'Auditoria em Segurança de SI', 'Status': 'Pendente', 'Área de atuação': 'Redes e Sistemas Computacionais', 'Tipo': 'Optativa', 'Pré-Requisitos': [8], "Crédito": 64},
        53: {'Nome': 'Computação em Nuvem', 'Status': 'Pendente', 'Área de atuação': 'Redes e Sistemas Computacionais', 'Tipo': 'Optativa', 'Pré-Requisitos': [8], "Crédito": 64},
        54: {'Nome': 'Programação Paralela', 'Status': 'Pendente', 'Área de atuação': 'Redes e Sistemas Computacionais', 'Tipo': 'Optativa', 'Pré-Requisitos': [8], "Crédito": 64},
        55: {'Nome': 'Sistemas Distribuidos', 'Status': 'Pendente', 'Área de atuação': 'Redes e Sistemas Computacionais', 'Tipo': 'Optativa', 'Pré-Requisitos': [8], "Crédito": 64},
        56: {'Nome': 'Tópicos em RSC', 'Status': 'Pendente', 'Área de atuação': 'Redes e Sistemas Computacionais', 'Tipo': 'Optativa', 'Pré-Requisitos': [8], "Crédito": 64},
        57: {'Nome': 'Simulação e Avaliação de Desempenho', 'Status': 'Pendente', 'Área de atuação': 'Redes e Sistemas Computacionais', 'Tipo': 'Optativa', 'Pré-Requisitos': [55], "Crédito": 32},
        58: {'Nome': 'Ciências Humanas e Sociais', 'Status': 'Pendente', 'Área de atuação': 'Aspectos Humanos em computação', 'Tipo': 'Optativa', 'Pré-Requisitos': [], "Crédito": 48},
        59: {'Nome': 'Psicologia: Relações índividuo-Grupo', 'Status': 'Pendente', 'Área de atuação': 'Aspectos Humanos em computação', 'Tipo': 'Optativa', 'Pré-Requisitos': [], "Crédito": 48},
        60: {'Nome': 'Ciências, Tecnologias e Organizações', 'Status': 'Pendente', 'Área de atuação': 'Aspectos Humanos em computação', 'Tipo': 'Optativa', 'Pré-Requisitos': [], "Crédito": 48},
        61: {'Nome': 'Comportamento Organizacional II', 'Status': 'Pendente', 'Área de atuação': 'Aspectos Humanos em computação', 'Tipo': 'Optativa', 'Pré-Requisitos': [], "Crédito": 32},
        62: {'Nome': 'Gestão de Carreira', 'Status': 'Pendente', 'Área de atuação': 'Aspectos Humanos em computação', 'Tipo': 'Optativa', 'Pré-Requisitos': [], "Crédito": 32},
        63: {'Nome': 'Psicologia Organizacional e Psicologia do Trabalho', 'Status': 'Pendente', 'Área de atuação': 'Aspectos Humanos em computação', 'Tipo': 'Optativa', 'Pré-Requisitos': [], "Crédito": 32},
        64: {'Nome': 'Tópicos em AHC', 'Status': 'Pendente', 'Área de atuação': 'Aspectos Humanos em computação', 'Tipo': 'Optativa', 'Pré-Requisitos': [], "Crédito": 64},
        65: {'Nome': 'Introdução à Administração', 'Status': 'Pendente', 'Área de atuação': 'Admnistração e Gestão', 'Tipo': 'Optativa', 'Pré-Requisitos': [], "Crédito": 32},
        66: {'Nome': 'Empreendedorismo e Inovação', 'Status': 'Pendente', 'Área de atuação': 'Admnistração e Gestão', 'Tipo': 'Optativa', 'Pré-Requisitos': [], 'Semestre': 1, "Crédito": 48},
        67: {'Nome': 'Comportamento Organizacional I', 'Status': 'Pendente', 'Área de atuação': 'Admnistração e Gestão', 'Tipo': 'Optativa', 'Pré-Requisitos': [], "Crédito": 48},
        68: {'Nome': 'Gestão e Governança de TI', 'Status': 'Pendente', 'Área de atuação': 'Admnistração e Gestão', 'Tipo': 'Optativa', 'Pré-Requisitos': [65], "Crédito": 64},
        69: {'Nome': 'Economia da Informação', 'Status': 'Pendente', 'Área de atuação': 'Admnistração e Gestão', 'Tipo': 'Optativa', 'Pré-Requisitos': [], "Crédito": 64},
        70: {'Nome': 'Empreendedorismo Técnológico', 'Status': 'Pendente', 'Área de atuação': 'Admnistração e Gestão', 'Tipo': 'Optativa', 'Pré-Requisitos': [66], "Crédito": 48},
        71: {'Nome': 'TCC1', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [], 'Co-Requisitos': [28], 'Semestre': 7, "Crédito": 140, 'Semestre Minimo': 5},
        72: {'Nome': 'TCC2', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos':[71], 'Semestre': 8, "Crédito": 210},
    }

    # For para analisar quais matérias já foram cursadas 
    for materia in grafoCCO.values():
        if materia['Nome'] in materias_cursadas.values():
            materia['Status'] = 'Cursada'

    return grafoCCO

def recomendar_materias_obrigatórias(grafoColorido, semestre_aluno = 1):
    materias_obrigatorias_pendentes = materias_pendentes_obrigatorias(grafoColorido)

    relevancia_materias_obrigatorias = {}
    for id in materias_obrigatorias_pendentes:
        # Armazena em uma lista o indice, número de relevância e a quantidade de materias as quais essa mesma matéria é pré-requisito
        relevancia_materias_obrigatorias[id] = definir_relevancia_materia(id, materias_obrigatorias_pendentes, semestre_aluno)

    return ranking_materias(relevancia_materias_obrigatorias, grafoColorido)

# Função responsável por listar os indíces das matérias obrigatórias que estão pendentes
def materias_pendentes_obrigatorias(grafoColorido):
    materias_pendentes_obrigatorias = {}

    for id, materia in grafoColorido.items():
        if materia['Tipo'] == 'Obrigatoria' and materia['Status'] == 'Pendente':
            materias_pendentes_obrigatorias[id] = materia

    return materias_pendentes_obrigatorias

def definir_relevancia_materia(id, materias_obrigatorias_pendentes, semestre_aluno):
    materia = materias_obrigatorias_pendentes[id]

    qtd_pre_requisito_materia = len(materia['Pré-Requisitos'])
    qtd_materia_atrasada = materia_atrasada(materia, semestre_aluno)
    qtd_materias_dependentes = contar_pre_requisitos(id, materias_obrigatorias_pendentes)

    return {
            'nome': materia['Nome'],
            'qtd_materia_atrasada': qtd_materia_atrasada,
            'qtd_pre_requisito_materia': qtd_pre_requisito_materia,
            'qtd_materias_dependentes': qtd_materias_dependentes,
            'semestre': materia['Semestre'],
            }

def materia_atrasada(materia, semestre_aluno):
    qtd_materia_atrasada = 0

    if (semestre_aluno > materia['Semestre'] and materia['Status'] == 'Pendente'):
        qtd_materia_atrasada = semestre_aluno - materia['Semestre']

    return qtd_materia_atrasada

def ranking_materias(lista_materias, grafoColorido):
    ranking = sorted(lista_materias.items(), key=lambda x: x[1]['qtd_materia_atrasada'] + x[1]['qtd_pre_requisito_materia'] + x[1]['qtd_materias_dependentes'] - x[1]['semestre'], reverse=True)

    materias_em_ordem = {}
    for id, _ in ranking:
        materias_em_ordem[id] = grafoColorido[id]

    return materias_em_ordem

def materias_pendentes_optativas(grafoColorido):
    optativas = {}
    for id, materia in grafoColorido.items():
        if materia['Tipo'] == 'Optativa' and materia['Status'] == 'Pendente':
            optativas[id] = materia

    return optativas

def ranking_materias_optativas(areas_de_conhecimento, grafo_optativas, optativas_em_ordem = {}):
    optativas_em_ordem = {}

    optativas = {}
    for area in areas_de_conhecimento:
        for id, materia in grafo_optativas.items():
            if materia['Área de atuação'] == area:
                optativas[id] = materia

        if len(optativas) == 0:
            continue 

        optativas = sorted(optativas.items(), key=lambda x: len(x[1]['Pré-Requisitos']), reverse=True)
        optativas_em_ordem.update(optativas)
        optativas = {}

    optativas = {}
    for id, materia in grafo_optativas.items():
        if materia['Área de atuação'] not in areas_de_conhecimento:
            optativas[id] = materia

        optativas = sorted(optativas.items(), key=lambda x: len(x[1]['Pré-Requisitos']), reverse=True)
        optativas_em_ordem.update(optativas)
        optativas = {}

        if len(optativas) == 0:
            continue 

    return optativas_em_ordem


def contar_pre_requisitos(id, materias_obrigatorias_pendentes):
    contador = 0

    for materia in materias_obrigatorias_pendentes.values():
        # Verifica se a matéria alvo é um pré-requisito para a matéria atual
        if id in materia['Pré-Requisitos']:
            contador += 1

    return contador

def montar_semestres(ranking_de_materias, ranking_optativas, semestres, semestre, materias_cursadas = {}):
    global horas_optativas_registradas

    while len(ranking_de_materias) > 0:
        id_materias_disponiveis = list(ranking_de_materias.keys())
        for id in id_materias_disponiveis:
            if id not in ranking_de_materias.keys():
                continue

            materia = ranking_de_materias[id]  
            # se o semestre está cheio, adiciona ele na lista de semestres e cria um novo semestre
            if semestre.isFull():
                semestres.append(semestre)
                semestre = semester.Semester(semestre.number + 1)
                break

            if esta_disponivel(materia, semestre) and pre_requisitos_alocados(semestres, materia, materias_cursadas): 
                if tem_correquisitos(materia) and adicionar_corrrequisitos(semestre, materia, ranking_de_materias) == False:
                    continue

                if semestre.AddMateria(id, materia):
                    del ranking_de_materias[id]

        # Quando acabar as matérias se o semestre não está vazio, adiciona ele na lista de semestres
        if semestre.isEmpty() == False:
            if horas_optativas_registradas < HORAS_OPTATIVAS and len(ranking_optativas) > 0:

                for id in list(ranking_optativas.keys()):
                    materia = ranking_optativas[id]
                    if semestre.isFull():
                        break

                    if semestre.AddMateria(id, materia):
                        horas_optativas_registradas += materia['Crédito']
                        del ranking_optativas[id]

            semestres.append(semestre)
            semestre = semester.Semester(semestre.number + 1)

    while horas_optativas_registradas < HORAS_OPTATIVAS: 
        for id in list(ranking_optativas.keys()):
            materia = ranking_optativas[id]

            if semestre.isFull():
                semestres.append(semestre)
                semestre = semester.Semester(semestre.number + 1)
                break

            if horas_optativas_registradas < HORAS_OPTATIVAS and semestre.AddMateria(id, materia):
                horas_optativas_registradas += materia['Crédito']
                del ranking_optativas[id]

        if semestre.isEmpty() == False:
            semestres.append(semestre)
            semestre = semester.Semester(semestre.number + 1) 

    return semestres

def adicionar_corrrequisitos(semestre, materia, ranking_de_materias):
    for id in materia['Co-Requisitos']:
        creditos_totais = semestre.currentCredits + materia['Crédito'] + ranking_de_materias[id]['Crédito']

        if creditos_totais > semestre.maxCredits or semestre.AddMateria(id, ranking_de_materias[id]) == False:
            return False

        del ranking_de_materias[id]

    return True

def esta_disponivel(materia, semester):
    if materia['Semestre'] % 2 == 0:
        if semester.isEven():
            return True
        return False

    if semester.isEven(): 
        return False

    if materia.get('Semestre Minimo', 0) > semester.number:
        return False

    return True

def pre_requisitos_alocados(semestres, materia, materias_cursadas):
    for pre_requisito in materia['Pré-Requisitos']:

        requisito_encontrado = False
        for semestre in semestres:
            for id in semestre.materias.keys():
                if id == pre_requisito: 
                    requisito_encontrado = True
                    break
            if requisito_encontrado:
                break

        if requisito_encontrado == False:
            if pre_requisito in materias_cursadas.keys():
                return True 
            else:
                return False
    
    return True

def tem_correquisitos(materia):
    return 'Co-Requisitos' in materia

def printDict(dictionary):
    print(json.dumps(dictionary, indent=2))

def main():
    semestreAtual = 1

    lista_materias_cursadas = {
            #0: 'Fundamentos de Programação',
            #10:'Arquitetura de Computadores I',
            #29:'Projeto Integrado',
            #21:'Matemática Discreta',
            #19:'Cálculo A'
    }

    #Execussão do Planejamento academico
    grafoColorido = define_materias_cursadas(lista_materias_cursadas)
    ranking_materias_obrigatorias = recomendar_materias_obrigatórias(grafoColorido, semestreAtual)
    ranking_optativas = ranking_materias_optativas(['Redes e Sistemas Computacionais'], materias_pendentes_optativas(grafoColorido))

    semesters = montar_semestres(ranking_materias_obrigatorias, ranking_optativas, [], semester.Semester(semestreAtual), lista_materias_cursadas)

    print("Horas Optativas: " + str(horas_optativas_registradas))
    print("Semestres:")
    printSemesters(semesters)


def printSemesters(semesters):
    for sems in semesters:
        print("\n" + "Semestre " + str(sems.number) + " Crédito: " + str(sems.currentCredits))

        for id, materia in sems.materias.items():
            print(id, materia['Nome'] + " " + materia['Tipo'] + " " + str(materia['Crédito'])+ " " + materia['Status'] + " " + materia['Área de atuação'] + " " +   str(materia.get('Semestre', 0)))
    print("\n")

if __name__ == "__main__":
    main()
