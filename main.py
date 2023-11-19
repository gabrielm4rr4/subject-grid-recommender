import matriz.matriz as matriz

import grades.cco as gradecco
import grades.sin as gradesin

import recomendador.semester as semester
import recomendador.recomendador as recomendador
import recomendador.materias_obrigatorias as materias_orbigatorias
import recomendador.materias_optativas as materias_optativas

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
    grafoColorido = gradecco.define_materias_cursadas(lista_materias_cursadas)
    matriz.gerar_matriz_area_atuacao(grafoColorido)
    matriz.gerar_matriz_de_prerequisitos(grafoColorido)

    ranking_materias_obrigatorias = materias_orbigatorias.recomendar_materias_obrigatórias(grafoColorido, semestreAtual)
    matriz.gerar_ordenacao_topologica(ranking_materias_obrigatorias)

    ranking_optativas = materias_optativas.ranking_materias_optativas(['Redes e Sistemas Computacionais'], materias_optativas.materias_pendentes_optativas(grafoColorido))
    matriz.gerar_ordenacao_topologica(ranking_optativas)

    semesters = recomendador.montar_semestres(ranking_materias_obrigatorias, ranking_optativas, [], semester.Semester(semestreAtual), lista_materias_cursadas)

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

