# Semester: Estrutura de dados que representa um semestre
class Semester:
    size = 0
    number = 0
    materias = {}

    def __init__(self, materias, size, number):
        self.size = size
        self.number = number
        self.materias = materias

    def AddMateria(self, id, materia):
        if self.isFull() == False:
            self.materias[id] = materia

    def isFull(self):
        return len(self.materias) == self.size

    def isEmpty(self):
        return len(self.materias) == 0

    def isEven(self):
        return self.number % 2 == 0

