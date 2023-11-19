import json
import random

from . import matriz
from . import gradecco
from . import gradesin
from . import semester

HORAS_OPTATIVAS = 672
horas_optativas_registradas = 0

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

    print("Horas Optativas: " + str(horas_optativas_registradas))
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
