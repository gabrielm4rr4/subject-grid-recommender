met_comp = 'blue'
adm_gestatão = 'orange'
asp_humanos_comp = 'gold'
dev_eng_software = 'yellow'
pers_analisis_dados = 'brown'
reder_sys_computacionais = 'red'

def areas_de_atuacao(materias):
    colors = {}
    for id, materia in materias.items():
        if materia['Status'] == 'Cursada':
            colors[id] = 'grey'
            continue

        if materia['Área de atuação'] == 'Desenvolvimento e Engenharia de Software':
            colors[id] = dev_eng_software
        elif materia['Área de atuação'] == 'Administração e Gestão de Tecnologia da Informação':
            colors[id] = adm_gestatão
        elif materia['Área de atuação'] == 'Metodologias Computacionais':
            colors[id] = met_comp
        elif materia['Área de atuação'] == 'Aspectos Humanos da Computação':
            colors[id] = asp_humanos_comp
        elif materia['Área de atuação'] == 'Perspectivas e Análises de Dados':
            colors[id] = pers_analisis_dados
        elif materia['Área de atuação'] == 'Redes e Sistemas Computacionais':
            colors[id] = reder_sys_computacionais

    return colors

def pre_requisitos(materias):
    colors = {}
    for id, materia in materias.items():
        if materia['Tipo'] == 'Obrigatoria':
            qtd_pre_requisitos = contar_pre_requisitos(id, materias)
            if qtd_pre_requisitos == 0:
                color = '#f5b8b8'
            elif qtd_pre_requisitos > 0 and qtd_pre_requisitos < 3:
                color = '#fc7979'
            elif qtd_pre_requisitos >= 3:
                color = '#fa0505'
        elif materia['Tipo'] == 'Optativa':
            color = 'green'

        colors[id] = color

    return colors

def contar_pre_requisitos(id, materias):
    contador = 0
    for materia in materias.values():
        # Verifica se a matéria alvo é um pré-requisito para a matéria atual
        if materia['Tipo'] == 'Obrigatoria' and id in materia['Pré-Requisitos']:
            contador += 1
    return contador


