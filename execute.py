
import matriz.matriz as matriz

import grades.cco as gradecco
import grades.sin as gradesin

import recomendador.semester as semester
import recomendador.recomendador as recomendador
import recomendador.materias_obrigatorias as materias_orbigatorias
import recomendador.materias_optativas as materias_optativas

def execute(semestre_atual, materias_cursadas, area_conhecimento_optativas, grade, gerar_matrizes = True):
    if grade == 'SIN':
        grafoColorido = gradesin.define_materias_cursadas(materias_cursadas)
    elif grade == 'CCO':
        grafoColorido = gradecco.define_materias_cursadas(materias_cursadas)
    else:
        print("Grade não encontrada")
        return

    ranking_obrigatorias = materias_orbigatorias.recomendar(grafoColorido, semestre_atual)
    ranking_optativas = materias_optativas.recomendar(area_conhecimento_optativas, materias_optativas.pendentes(grafoColorido))

    if gerar_matrizes:
        matriz.gerar_matriz_area_atuacao(grafoColorido)
        matriz.gerar_matriz_de_prerequisitos(grafoColorido)
        pendentes_obrigatorias = materias_orbigatorias.materias_pendentes_obrigatorias(grafoColorido)
        pendentes_obrigatorias = sorted(pendentes_obrigatorias.items(), key=lambda x: len(x[1]['Pré-Requisitos']))
        matriz.gerar_ordenacao_topologica(matriz.ordenar_topologicamente(pendentes_obrigatorias))

    semesters = recomendador.montar_semestres(
            ranking_obrigatorias, 
            ranking_optativas, 
            semestre_atual, 
            materias_cursadas,
            )

    printSemesters(semesters)

def printSemesters(semesters):
    for sems in semesters:
        print("\n" + "Semestre " + str(sems.number) + " Crédito: " + str(sems.currentCredits))

        for id, materia in sems.materias.items():
            print(materia.get('Código', 0), materia['Nome'] + " " + materia['Tipo'] + " " + str(materia['Crédito'])+ " " + materia['Status'] + " " + str(materia.get('Semestre', 0)))
    print("\n")
