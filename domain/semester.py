# Semester: Estrutura de dados que representa um semestre
class Semester:
    number = 0
    materias = {}
    maxCredits = 400
    currentCredits = 0

    def __init__(self, number):
        self.number = number
        self.materias = {}
        self.currentCredits = 0

    def AddMateria(self, id, materia):
        if self.currentCredits + materia['Crédito'] > self.maxCredits:
            return False

        self.materias[id] = materia
        self.currentCredits += materia['Crédito']
        return True

    def isFull(self):
        return self.maxCredits - self.currentCredits < 32

    def isEmpty(self):
        return len(self.materias) == 0

    def isEven(self):
        return self.number % 2 == 0

