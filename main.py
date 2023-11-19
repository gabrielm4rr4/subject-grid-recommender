import matriz.matriz as matriz

import grades.cco as gradecco
import grades.sin as gradesin

import recomendador.semester as semester
import recomendador.recomendador as recomendador
import recomendador.materias_obrigatorias as materias_orbigatorias
import recomendador.materias_optativas as materias_optativas

def main():
    semestre_atual = 1
    gerar_matrizes = True
    materias_cursadas = {
            #0: 'Fundamentos de Programação',
            #10:'Arquitetura de Computadores I',
            #29:'Projeto Integrado',
            #21:'Matemática Discreta',
            #19:'Cálculo A'
    }

    area_conhecimento_optativas = ['Redes e Sistemas Computacionais']

    #Execussão do Planejamento academico
    grafoColorido = gradecco.define_materias_cursadas(materias_cursadas)
    ranking_obrigatorias = materias_orbigatorias.recomendar(grafoColorido, semestre_atual)
    ranking_optativas = materias_optativas.recomendar(area_conhecimento_optativas, materias_optativas.pendentes(grafoColorido))

    if gerar_matrizes:
        matriz.gerar_matriz_area_atuacao(grafoColorido)
        matriz.gerar_matriz_de_prerequisitos(grafoColorido)
        matriz.gerar_ordenacao_topologica(ranking_obrigatorias)
        matriz.gerar_ordenacao_topologica(ranking_optativas)


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
            print(id, materia['Nome'] + " " + materia['Tipo'] + " " + str(materia['Crédito'])+ " " + materia['Status'] + " " + materia['Área de atuação'] + " " +   str(materia.get('Semestre', 0)))
    print("\n")

if __name__ == "__main__":
    main()
