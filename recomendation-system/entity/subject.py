# Subject: representa a entidade da matéria a ser cursada
class Subject:
    id = 0
    name = ""
    main_area = ""
    required = False
    prerequisites = []
    status = "Pendente"
    semester = 0

    def __init__(self, id, name, main_area, required, status, prerequisites, semester):
        self.id = id
        self.name = name
        self.main_area = main_area
        self.required = required
        self.status = status
        self.prerequisites = prerequisites
        self.semester = semester

    def isFinished(self):
        return self.status == "Aprovado"

    def setFinished(self):
        self.status = "Aprovado"

    def isAvaliable(self, semester):
        if self.semester % 2 == 0:
            if semester.isEven():
                return True
            return False
        
        if semester.isEven(): 
            return False
        return True
