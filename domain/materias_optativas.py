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



