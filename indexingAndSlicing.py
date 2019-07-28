import pandas as pd

notes = pd.read_csv("grades.csv")

notes.columns = ["First name","Last name",
                 "SSN","Test1", "Test2",
                 "Test3", "Test4",
                 "Final", "Grade"]
print(notes)
print(notes.loc[:,"First name"])
print(notes.loc[:5,"First name"])
print(notes.loc[:5,"First name":"Test4"])
print(notes.loc[:5,["First name","Final","Grade"]])
print(notes.loc[:5,:"Test2"])
print(notes.loc[::-1,:"First name"])
