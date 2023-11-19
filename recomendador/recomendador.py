import json
import random

from . import semester

MIN_HORAS_OPTATIVAS = 672
horas_optativas_registradas = 0

def montar_semestres(ranking_de_materias, ranking_optativas, semestre_atual, materias_cursadas):
    semestres = []
    semestre = semester.Semester(semestre_atual)

    inserir_materias_obrigatorias_e_optativas(ranking_de_materias, ranking_optativas, semestres, semestre, materias_cursadas)
    inserir_materias_optativas_restantes(ranking_optativas, semestres, semestre)

    print("Horas Optativas: " + str(horas_optativas_registradas))
    return semestres

# Insere as matérias obrigatórias e optativas nos semestres:
# insere matérias obrigatórias prioritárias primeiro
# caso sobre carga horária e não hajá mais nenhuma matéria obrigatória que possa ser inserida,
# então insere matérias optativas
def inserir_materias_obrigatorias_e_optativas(ranking_de_materias, ranking_optativas, semestres, semestre, materias_cursadas):

    while len(ranking_de_materias) > 0:
        for id in list(ranking_de_materias.keys()):

            if id not in ranking_de_materias.keys():
                continue

            materia = ranking_de_materias[id]  

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
            if pode_adicionar_optativas_ao_semestre(ranking_optativas):
                semestre = adiciona_optativas_ao_semestre(ranking_optativas, semestre)
            semestres.append(semestre)
            semestre = semester.Semester(semestre.number + 1)

    return semestres

def esta_disponivel(materia, semester):
    if materia.get('Semestre Minimo', 0) > semester.number:
        return False

    if materia['Semestre'] % 2 == 0:
        if semester.isEven():
            return True
        return False

    if semester.isEven():
        return False 

    return True

def pre_requisitos_alocados(semestres, materia, materias_cursadas):
    for pre_requisito in materia['Pré-Requisitos']:
        requisito_encontrado = False

        # Busca nos semestres anteriores
        for semestre in semestres:
            for id in semestre.materias.keys():
                if pre_requisito == id: 
                    requisito_encontrado = True
                    break

            if requisito_encontrado:
                break

        # Caso não tenha achado ainda busca nas matérias cursadas
        if requisito_encontrado == False:
            if pre_requisito in materias_cursadas.keys():
                return True 
            return False
    
    return True

def tem_correquisitos(materia):
    return 'Co-Requisitos' in materia

def adicionar_corrrequisitos(semestre, materia, ranking_de_materias):
    for id in materia['Co-Requisitos']:

        # creditos totais = creditos atuais do semestre + créditos da matéria que possui correquisito + créditos do correquisito
        creditos_totais = semestre.currentCredits + materia['Crédito'] + ranking_de_materias[id]['Crédito']

        if creditos_totais > semestre.maxCredits or semestre.AddMateria(id, ranking_de_materias[id]) == False:
            return False

        del ranking_de_materias[id]

    return True

def pode_adicionar_optativas_ao_semestre(ranking_optativas):
    return faltam_horas_optativas() and len(ranking_optativas) > 0

def faltam_horas_optativas():
    return horas_optativas_registradas < MIN_HORAS_OPTATIVAS

def adiciona_optativas_ao_semestre(ranking_optativas, semestre):
    global horas_optativas_registradas

    for id in list(ranking_optativas.keys()):
        materia = ranking_optativas[id]

        if semestre.AddMateria(id, materia):
            horas_optativas_registradas += materia['Crédito']
            del ranking_optativas[id]

        if semestre.isFull():
            break

    return semestre

# Após todas as orbigatórias terem sido inseridas
# caso ainda falte horas optativas
# insere as matérias optativas restantes até completar as horas optativas
def inserir_materias_optativas_restantes(ranking_optativas, semestres, semestre):
    global horas_optativas_registradas

    while faltam_horas_optativas(): 
        for id in list(ranking_optativas.keys()):
            materia = ranking_optativas[id]

            if faltam_horas_optativas() and semestre.AddMateria(id, materia):
                horas_optativas_registradas += materia['Crédito']
                del ranking_optativas[id]

            if semestre.isFull():
                semestres.append(semestre)
                semestre = semester.Semester(semestre.number + 1)
                break

        if semestre.isEmpty() == False:
            semestres.append(semestre)
            semestre = semester.Semester(semestre.number + 1) 


