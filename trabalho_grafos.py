import json
import random
import semester
import subject

HORAS_OPTATIVAS = 672

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
        30: {'Nome': 'Arquitetura de Software', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [], "Crédito": 64},
        31: {'Nome': 'Padrões de Projeto', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [37], "Crédito": 64},
        32: {'Nome': 'Engenharia de Software Experimental', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [], "Crédito": 64},
        33: {'Nome': 'Tópicos em DES I', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [], "Crédito": 64},
        34: {'Nome': 'Tópicos em DES II', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [], "Crédito": 64},
        35: {'Nome': 'Desenvolvimento de Jogos', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [], "Crédito": 64},
        36: {'Nome': 'Desenvolvimento para Dispositivos Móveis', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [], "Crédito": 64},
        37: {'Nome': 'Reutilização de Software', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [], "Crédito": 64},
        38: {'Nome': 'Engenharia de Software II', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [37, 39], "Crédito": 64},
        39: {'Nome': 'Gerência de projetos de software', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [], "Crédito": 64},
        40: {'Nome': 'Desenvolvimento de sistemas web', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [], "Crédito": 64},
        41: {'Nome': 'Maratona de programação I', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [42], "Crédito": 48},
        42: {'Nome': 'Maratona de programação II', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [], "Crédito": 48},
        43: {'Nome': 'Banco de Dados II', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [], "Crédito": 64},
        44: {'Nome': 'Introdução à Análise de Dados', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [46], "Crédito": 64},
        45: {'Nome': 'Banco de Dados noSQL', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [], "Crédito": 64},
        46: {'Nome': 'Tópicos em PAD', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [], "Crédito": 64},
        47: {'Nome': 'Modelagem Geométrica e Visual', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [], "Crédito": 64},
        48: {'Nome': 'Visão Computacional', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [], "Crédito": 64},
        49: {'Nome': 'Métodos Exatos', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [], "Crédito": 64},
        50: {'Nome': 'Metaheurísticas', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [], "Crédito": 64},
        51: {'Nome': 'Tópicos em MCO', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [], "Crédito": 64},
        52: {'Nome': 'Auditoria em Segurança de SI', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [], "Crédito": 64},
        53: {'Nome': 'Computação em Nuvem', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [], "Crédito": 64},
        54: {'Nome': 'Programação Paralela', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [], "Crédito": 64},
        55: {'Nome': 'Sistemas Distribuidos', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [57], "Crédito": 64},
        56: {'Nome': 'Tópicos em RSC', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [], "Crédito": 64},
        57: {'Nome': 'Simulação e Avaliação de Desempenho', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [], "Crédito": 32},
        58: {'Nome': 'Ciências Humanas e Sociais', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [], "Crédito": 48},
        59: {'Nome': 'Psicologia: Relações índividuo-Grupo', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [], "Crédito": 48},
        60: {'Nome': 'Ciências, Tecnologias e Organizações', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [], "Crédito": 48},
        61: {'Nome': 'Comportamento Organizacional II', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [], "Crédito": 32},
        62: {'Nome': 'Gestão de Carreira', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [], "Crédito": 32},
        63: {'Nome': 'Psicologia Organizacional e Psicologia do Trabalho', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [], "Crédito": 32},
        64: {'Nome': 'Tópicos em AHC', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [], "Crédito": 64},
        65: {'Nome': 'Introdução à Administração', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [68], "Crédito": 32},
        66: {'Nome': 'Empreendedorismo e Inovação', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [70], 'Semestre': 1, "Crédito": 48},
        67: {'Nome': 'Comportamento Organizacional I', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [], "Crédito": 48},
        68: {'Nome': 'Gestão e Governança de TI', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [], "Crédito": 64},
        69: {'Nome': 'Economia da Informação', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [], "Crédito": 64},
        70: {'Nome': 'Empreendedorismo Técnológico', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [], "Crédito": 48},
        71: {'Nome': 'TCC1', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [], 'Co-Requisitos': [28], 'Semestre': 7, "Crédito": 140, 'Semestre Minimo': 5},
        72: {'Nome': 'TCC2', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos':[71], 'Semestre': 8, "Crédito": 210},
    }

    # For para analisar quais matérias já foram cursadas 
    for materia in grafoCCO.values():
        if materia['Nome'] in materias_cursadas.values():
            materia['Status'] = 'Cursada'

    return grafoCCO

# Função para recomendar matérias optativas com base nas informações do estudante
def recomendar_materias_optativas(G, area_desejada):

    # 1) Essas matéria é da área de atuação do interesse do aluno?
    identificacao_area_de_atuacao(indice,grafoColorido)

    pass

def identificacao_area_de_atuacao (indice_materia, grafoColorido):
    pass

def recomendar_materias_obrigatórias(grafoColorido, semestre_aluno = 1):
    lista_materias_pendentes_obrigatorias = materias_pendentes_obrigatorias(grafoColorido)

    relevancia_materias_obrigatorias = {}
    for id in lista_materias_pendentes_obrigatorias:
        # Armazena em uma lista o indice, número de relevância e a quantidade de materias as quais essa mesma matéria é pré-requisito
        relevancia_materias_obrigatorias[id] = definir_relevancia_materia(id, grafoColorido, semestre_aluno)

    return ranking_materias(relevancia_materias_obrigatorias, grafoColorido)

# Função responsável por listar os indíces das matérias obrigatórias que estão pendentes
def materias_pendentes_obrigatorias(grafoColorido):
    indices_materias_pendentes_obrigatorias = []

    for indice, materia in grafoColorido.items():
        if materia['Tipo'] == 'Obrigatoria' and materia['Status'] == 'Pendente':
            indices_materias_pendentes_obrigatorias.append(indice)

    return indices_materias_pendentes_obrigatorias

def definir_relevancia_materia(id, grafoColorido, semestre_aluno):
    materia = grafoColorido[id]

    qtd_pre_requisito_materia = len(materia['Pré-Requisitos'])
    qtd_materia_atrasada = materia_atrasada(materia, semestre_aluno)
    qtd_materias_dependentes = contar_pre_requisitos(id, grafoColorido)

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


def contar_pre_requisitos(id, grafoColorido):
    contador = 0

    for materia in grafoColorido.values():
        # Verifica se a matéria alvo é um pré-requisito para a matéria atual
        if id in materia['Pré-Requisitos']:
            contador += 1

    return contador

def montar_semestres(ranking_de_materias, semestres, semestre, materias_cursadas = {}):
    while len(ranking_de_materias) > 0:
        for id in list(ranking_de_materias.keys()):
            materia = ranking_de_materias[id]
            # se o semestre está cheio, adiciona ele na lista de semestres e cria um novo semestre
            if semestre.isFull():
                semestres.append(semestre)
                semestre = semester.Semester(semestre.number + 1)
                break

            if esta_disponivel(materia, semestre) and pre_requisitos_alocados(semestres, materia, materias_cursadas): 
                if semestre.AddMateria(id, materia):
                    del ranking_de_materias[id]

        # Quando acabar as matérias se o semestre não está vazio, adiciona ele na lista de semestres
        if semestre.isEmpty() == False:
            semestres.append(semestre)
            semestre = semester.Semester(semestre.number + 1)

    return semestres

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
                if id  == pre_requisito: 
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


def printDict(dictionary):
    print(json.dumps(dictionary, indent=2))

def main():
    semestreAtual = 3

    lista_materias_cursadas = {
            0: 'Fundamentos de Programação',
            10: 'Arquitetura de Computadores I',
            29: 'Projeto Integrado',
            21:'Matemática Discreta',
            19:'Cálculo A'
    }

    #Execussão do Planejamento academico
    grafoColorido = define_materias_cursadas(lista_materias_cursadas)
    ranking_materias_obrigatorias = recomendar_materias_obrigatórias(grafoColorido, semestreAtual)

    semesters = montar_semestres(ranking_materias_obrigatorias, [], semester.Semester(semestreAtual), lista_materias_cursadas)

    print("Semestres:")
    printSemesters(semesters)


def printSemesters(semesters):
    for sems in semesters:
        print("\n" + "Semestre " + str(sems.number) + " Crédito: " + str(sems.currentCredits))

        for id, materia in sems.materias.items():
            print(id, materia['Nome'] + " " + " " + str(materia['Crédito'])+ " " + materia['Status'] + " " + str(materia['Semestre']))
    print("\n")

if __name__ == "__main__":
    main()
