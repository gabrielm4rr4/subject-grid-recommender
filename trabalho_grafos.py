# Função que percorre o grafo e define as matérias já cursadas
def define_materias_cursadas(materias_cursadas):
    # Colore o grafo inicial com todas matérias com status "Pendente" e define como "Cursadas" caso esteja na lista de "materias_cursadas" dada no input do aluno
    dicionarioMaterias = {
        0: {'Nome': 'Fundamentos de Programação', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [1, 13, 35, 71]},
        1: {'Nome': 'Programação Orientada a Objetos', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [2, 7, 15, 37, 71]},
        2: {'Nome': 'Programação Web', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [27, 31, 36, 40, 71]},
        3: {'Nome': 'Engenharia de Software I', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [30, 31, 32, 33, 34, 38, 40, 71]},
        4: {'Nome': 'Programação Lógica e Funcional', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [17, 71]},
        5: {'Nome': 'Banco de Dados I', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [40, 43, 45, 46, 71]},
        6: {'Nome': 'Inteligência Artificial', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [71]},
        7: {'Nome': 'Introdução à Computação Visual', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [47, 48, 71]},
        8: {'Nome': 'Redes de Computadores', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [52, 53, 54, 55, 56, 71]},
        9: {'Nome': 'Sistemas Operacionais', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [8, 71]},
        10: {'Nome': 'Arquitetura de Computadores I', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [11, 71]},
        11: {'Nome': 'Arquitetura de Computadores II', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [9, 12, 71]},
        12: {'Nome': 'Sistemas Embarcados', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [71]},
        13: {'Nome': 'Algoritmos e Estruturas de Dados I', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [9, 12, 14, 22, 23, 41, 71]},
        14: {'Nome': 'Algoritmos e Estruturas de Dados II', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [5, 16, 71]},
        15: {'Nome': 'Análise e Projeto Orientados a Objeto', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [71]},
        16: {'Nome': 'Projeto e Análise de Algoritmos', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [17, 71]},
        17: {'Nome': 'Teoria da Computação', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [18]},
        18: {'Nome': 'Compiladores', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': []},
        19: {'Nome': 'Cálculo A', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [7, 20, 22, 24, 25, 71]},
        20: {'Nome': 'Cálculo B', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [71]},
        21: {'Nome': 'Matemática Discreta', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [4, 22, 48, 71]},
        22: {'Nome': 'Métodos Matemáticos para Análise de Dados', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [6, 44, 47, 49, 50, 51, 71]},
        23: {'Nome': 'Algoritmos em Grafos', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [16, 49, 50, 51, 71]},
        24: {'Nome': 'Modelagem Computacional', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': []},
        25: {'Nome': 'Cálculo Numérico para Computação', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [47, 48]},
        26: {'Nome': 'Computação e Sociedade', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': []},
        27: {'Nome': 'Interação Humano-Computador', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': []},
        28: {'Nome': 'Metodologia Científica', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': []},
        29: {'Nome': 'Projeto Integrado', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [71]},
        30: {'Nome': 'Arquitetura de Software', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': []},
        31: {'Nome': 'Padrões de Projeto', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [37]},
        32: {'Nome': 'Engenharia de Software Experimental', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': []},
        33: {'Nome': 'Tópicos em DES I', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': []},
        34: {'Nome': 'Tópicos em DES II', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': []},
        35: {'Nome': 'Desenvolvimento de Jogos', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': []},
        36: {'Nome': 'Desenvolvimento para Dispositivos Móveis', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': []},
        37: {'Nome': 'Reutilização de Software', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': []},
        38: {'Nome': 'Engenharia de Software II', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [37, 39]},
        39: {'Nome': 'Gerência de projetos de software', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': []},
        40: {'Nome': 'Desenvolvimento de sistemas web', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': []},
        41: {'Nome': 'Maratona de programação I', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [42]},
        42: {'Nome': 'Maratona de programação II', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': []},
        43: {'Nome': 'Banco de Dados II', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': []},
        44: {'Nome': 'Introdução à Análise de Dados', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [46]},
        45: {'Nome': 'Banco de Dados noSQL', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': []},
        46: {'Nome': 'Tópicos em PAD', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': []},
        47: {'Nome': 'Modelagem Geométrica e Visual', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': []},
        48: {'Nome': 'Visão Computacional', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': []},
        49: {'Nome': 'Métodos Exatos', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': []},
        50: {'Nome': 'Metaheurísticas', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': []},
        51: {'Nome': 'Tópicos em MCO', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': []},
        52: {'Nome': 'Auditoria em Segurança de SI', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': []},
        53: {'Nome': 'Computação em Nuvem', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': []},
        54: {'Nome': 'Programação Paralela', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': []},
        55: {'Nome': 'Sistemas Distribuidos', 'status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [57]},
        56: {'Nome': 'Tópicos em RSC', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': []},
        57: {'Nome': 'Simulação e Avaliação de Desempenho', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': []},
        58: {'Nome': 'Ciências Humanas e Sociais', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': []},
        59: {'Nome': 'Psicologia: Relações índividuo-Grupo', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': []},
        60: {'Nome': 'Ciências, Tecnologias e Organizações', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': []},
        61: {'Nome': 'Comportamento Organizacional II', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': []},
        62: {'Nome': 'Gestão de Carreira', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': []},
        63: {'Nome': 'Psicologia Organizacional e Psicologia do Trabalho', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': []},
        64: {'Nome': 'Tópicos em AHC', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': []},
        65: {'Nome': 'Introdução à Administração', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [68]},
        66: {'Nome': 'Empreendedorismo e Inovação', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': [70]},
        67: {'Nome': 'Comportamento Organizacional I', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': []},
        68: {'Nome': 'Gestão e Governança de TI', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': []},
        69: {'Nome': 'Economia da Informação', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': []},
        70: {'Nome': 'Empreendedorismo Técnológico', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Optativa', 'Pré-Requisitos': []},
        71: {'Nome': 'TCC1', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos': [72]},
        72: {'Nome': 'TCC2', 'Status': 'Pendente', 'Área de atuação': '', 'Tipo': 'Obrigatoria', 'Pré-Requisitos':[]}
    }
    
    return grafo_atualizado
    
# Função para recomendar matérias optativas com base nas informações do estudante
def recomendar_materias_optativas(G, area_desejada):
    arrayOptativasPrimario = [] # Optativas da área de conhecimento desejada
    arrayOptativasSecundario = [] # Optativas fora da área de conhecimento

    for node, data in G.nodes(data=True):
        if data['tipo'] == 'optativa' and data['area_conhecimento'] == area_desejada: #Verificar somente não cursadas
            arrayOptativasPrimario.append(node)

    # Criar o laço de repetição que acrescenta as matérias no segundo array
    # Critérios serão: matéria é ofertada no semestre atual, não é obrigatória, não é da área de conhecimento desejada

    return arrayOptativasPrimario, arrayOptativasSecundario

# Função para recomendar matérias obrigatórias com base nas informações do estudante
def recomendar_materias_obrigatórias(G, ano_ingresso, ano, semestre, materias_cursadas, area_prioritaria):
    # Lógica para recomendação de matérias com base nos parâmetros fornecidos
    # Aqui, você pode implementar a lógica específica para recomendar matérias com base nos critérios desejados

    # Aqui serão chamada as várias funções que vamos usar pra verificar o grafo e recomendar as matérias

    # Retornar um array de objetos, no qual cada posição será referente a uma matéria que deve ser cursada
    # Os atributos de cada objeto serão: nome da matéria, código da matéria, periodo(semestre) ofertada
    # relevância (montar uma lista que irá definir a importância de cursar essa matéria 0 - 10), legenda (motivo da matéria ter sido selecionada)

    # Com base no grau de relevância calculado, preparar uma mensagem pré-definida do motivo

    arrayObrigatóriasLimite = [] # Matérias obrigatórias ordenadas pelo grau de relevância respeitando o limite de matérias definido pelo usuário
    arrayObrigatóriasExtra = [] # Restante das matérias obrigatórias que ele pode puxar no semestre que ficaram de fora do array principal
    # por terem grau de relevância menor do que as primeiras, mas servem como segunda opção caso haja conflito de horário ou qualquer outro impedimento
    return arrayObrigatóriasLimite, arrayObrigatóriasExtra


# Exemplo de inputs do usuário (não implementados aqui, é necessário adaptar para entrada real do usuário)
ano_ingresso = 2022
ano = 2 # Ano correspondente do curso - Segundo ano
semestre = 1
materias_cursadas = []  # Lista de matérias já cursadas pelo estudante (pode ser um JSON)
area_prioritaria = 'Ciências Exatas'
limite_materias_semestre = 5

# Chamando as funções para recomendar matérias com base nas informações do estudante. Montar um output para exibi-las
arrayObrigatórias = recomendar_materias_obrigatórias(grafo_materias, ano_ingresso, ano, semestre, materias_cursadas, area_prioritaria)
arrayOptativas = recomendar_materias_optativas(grafo_materias, area_prioritaria)
