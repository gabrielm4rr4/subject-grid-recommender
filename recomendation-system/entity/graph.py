from entity import subject
from entity import semester

# Graph guarda o grafo da matéria e faz operações em cima dele
class Graph:
    subjects = []

    # __init__: inicializa o grafo com as matérias do curso
    def __init__(self, subjects):
        parsedSubjects = [] 
        for id, s in subjects.items():
            required = False
            if s["Tipo"] == "Obrigatoria":
                required = True

            sub = subject.Subject(id, s["Nome"], s["Área de atuação"], required, s["Status"], s["Pré-Requisitos"], s.get("Semestre", 0))

            parsedSubjects.append(sub)

        self.subjects = parsedSubjects

    # BuildRequiredTopologicalOrder: retorna uma lista de matérias obrigatórias pendentes em ordem topológica
    def BuildRequiredTopologicalOrder(self):
        topologicalOrder = []
        requiredSubjects = self.sortBySemester(self.GetRequiredSubjectsPending())

        for s in requiredSubjects:
            topologicalOrder.append(s)

        return topologicalOrder

    # GetRequiredSubjectsPending: retorna as matérias obrigatórias pendentes
    def GetRequiredSubjectsPending(self):
        requiredPendingSubjects = []
        for s in self.subjects:
            if s.required and s.status == "Pendente":
                requiredPendingSubjects.append(s)

        return requiredPendingSubjects

    # sortBySemester: ordena as matérias por semestre
    def sortBySemester(self, subjects):
        subjects.sort(key=lambda x: x.semester) 
        return subjects

    # ProcessFinishedSubjects: marca as matérias que já foram cursadas como aprovadas 
    def ProcessFinishedSubjects(subjects, finished_subjects):
        for k, s in subjects.items():
            if s.name in finished_subjects:
                s.setFinished()

        return subjects

    # BuildSubjectsSemesterRecommendation: retorna uma lista de semestres com as matérias pendentes
    # alocadas em cada semestre
    def BuildSubjectsSemesterRecommendation(self):
        topologicalOrder = self.BuildRequiredTopologicalOrder()

        return self.buildSemesters(topologicalOrder, [], semester.Semester([], 5, 1))

    # buildSemesters: aloca as matérias em semestres
    def buildSemesters(self, subjects, semesters, sem):
        subsNotAvalableAtTheMoment = []

        for s in subjects:
            # se o semestre está cheio, adiciona ele na lista de semestres e cria um novo semestre
            if sem.isFull():
                semesters.append(sem)
                sem = semester.Semester([], 5, sem.number + 1)

            # checka se a matéria está disponível para ser cursada no semestre atual
            # checka se a matéria tem todos os pré-requisitos necessários para ser cursada
            if s.isAvaliable(sem) and hasAllPrerequisits(semesters, s): 
                sem.AddSubject(s)
            else:
                subsNotAvalableAtTheMoment.append(s)

        
        # Quando acabar as matérias se o semestre não está vazio, adiciona ele na lista de semestres
        if sem.isEmpty() == False:
            semesters.append(sem)


        # se não tem mais matérias para serem alocadas, retorna a lista de semestres
        if len(subsNotAvalableAtTheMoment) == 0:
            return semesters

        # se ainda tem matérias para serem alocadas, chama a função recursivamente
        return self.buildSemesters(subsNotAvalableAtTheMoment, semesters, semester.Semester([], 5, sem.number + 1))

# hasAllPrerequisits: verifica se os semestres passados tem todos os pré-requisitos
# necessários para cursar a matéria q está querendo ser adicionada
def hasAllPrerequisits(semesters, subject):
    for requisit in subject.prerequisites:

        hasRequisit = False
        for sem in semesters:
            for s in sem.subjects:
                if s.id  == requisit: 
                    hasRequisit = True
                    break
            if hasRequisit:
                break

        if hasRequisit == False:
            return False

    return True

