import classes
from entity import graph

graph = graph.Graph(classes.define_materias_cursadas()) 

semesters = graph.BuildSubjectsSemesterRecommendation()

for sems in semesters:
    print("\n" + "Semestre " + str(sems.number))
    for s in sems.subjects:
        print(s.name + " " + s.status + " " + str(s.semester))

