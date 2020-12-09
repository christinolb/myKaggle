import pandas as pd

stuPerf = pd.read_csv("StudentsPerformance.csv")
studentsP = pd.DataFrame(stuPerf)

print(studentsP["gender"] == "male")
