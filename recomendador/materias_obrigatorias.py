def recomendar(grafoColorido, semestre_aluno = 1):
    materias_obrigatorias_pendentes = materias_pendentes_obrigatorias(grafoColorido)

    relevancia_materias_obrigatorias = {}
    for id in materias_obrigatorias_pendentes:
        relevancia_materias_obrigatorias[id] = definir_relevancia_materia(id, materias_obrigatorias_pendentes, semestre_aluno)

    return ranking_materias(relevancia_materias_obrigatorias, grafoColorido)

def materias_pendentes_obrigatorias(grafoColorido):
    materias_pendentes_obrigatorias = {}

    for id, materia in grafoColorido.items():
        if materia['Tipo'] == 'Obrigatoria' and materia['Status'] == 'Pendente':
            materias_pendentes_obrigatorias[id] = materia

    return materias_pendentes_obrigatorias


# Relevância da matéria é dada pelos seguintes dados:
# semestre - Relevância é Inversamente Proporcial
# qtd_pre_requisito_materia - Relevância Diretamente Proporcional
# qtd_materia_atrasada - Relevância Diratemente Proporcional
# qtd_materias_dependentes - Relenvância Diretamente Proporcional
def definir_relevancia_materia(id, materias_obrigatorias_pendentes, semestre_aluno):
    materia = materias_obrigatorias_pendentes[id]

    return {
            'semestre': materia['Semestre'],
            'qtd_pre_requisito_materia': len(materia['Pré-Requisitos']),
            'qtd_materia_atrasada': materia_atrasada(materia, semestre_aluno),
            'qtd_materias_dependentes': contar_pre_requisitos(id, materias_obrigatorias_pendentes),
            }

def materia_atrasada(materia, semestre_aluno):
    qtd_materia_atrasada = 0

    if (semestre_aluno > materia['Semestre'] and materia['Status'] == 'Pendente'):
        qtd_materia_atrasada = semestre_aluno - materia['Semestre']

    return qtd_materia_atrasada

def contar_pre_requisitos(id, materias_obrigatorias_pendentes):
    contador = 0

    for materia in materias_obrigatorias_pendentes.values():
        # Verifica se a matéria atual é um pré-requisito para alguma outra matéria
        if id in materia['Pré-Requisitos']:
            contador += 1

    return contador

# O rankiamento das matérias é feito através do cálculo: 
# Relevancia Total: qtd_materia_atrasada + qtd_pre_requisito_materia + qtd_materias_dependentes - semestre
# Quanto maior o valor, maior a relevância da matéria
def ranking_materias(lista_materias, grafoColorido):
    ranking = sorted(lista_materias.items(), key=lambda x: x[1]['qtd_materia_atrasada'] + x[1]['qtd_pre_requisito_materia'] + x[1]['qtd_materias_dependentes'] - x[1]['semestre'], reverse=True)

    materias_em_ordem = {}
    for id, _ in ranking:
        materias_em_ordem[id] = grafoColorido[id]

    return materias_em_ordem
