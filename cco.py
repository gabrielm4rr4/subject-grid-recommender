import execute

def main():
    semestre_atual = 3

    materias_cursadas = {
            0: 'Fundamentos de Programação',
            10:'Arquitetura de Computadores I',
            29:'Projeto Integrado',
            21:'Matemática Discreta',
            19:'Cálculo A'
    }

    area_conhecimento_optativas = ['Redes e Sistemas Computacionais']

    execute.execute(semestre_atual, materias_cursadas, area_conhecimento_optativas, 'CCO', False)

if __name__ == "__main__":
    main()
