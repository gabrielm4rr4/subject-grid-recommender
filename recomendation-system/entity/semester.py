# Semester: Estrutura de dados que representa um semestre
class Semester:
    size = 0
    number = 0
    subjects = []

    def __init__(self, subjects, size, number):
        self.size = size
        self.number = number
        self.subjects = subjects

    def AddSubject(self, subject):
        if self.isFull() == False:
            self.subjects.append(subject)

    def isFull(self):
        return len(self.subjects) == self.size

    def isEmpty(self):
        return len(self.subjects) == 0

    def isEven(self):
        return self.number % 2 == 0

