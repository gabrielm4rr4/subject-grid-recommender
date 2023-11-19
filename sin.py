import execute

def main():
    semestre_atual = 1

    gerar_matrizes = True

    materias_cursadas = {
            #0: 'Fundamentos de Programação',
    }

    area_conhecimento_optativas = []

    execute.execute(semestre_atual, materias_cursadas, area_conhecimento_optativas, 'SIN', True)

if __name__ == "__main__":
    main()
