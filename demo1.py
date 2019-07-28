
import pandas as pd

notes = pd.read_csv("grades.csv")

notes.columns = ["First name","Last name",
                 "SSN","Test1", "Test2",
                 "Test3", "Test4",
                 "Final", "Grade"]

print(notes)

print(notes.head())
print()
print(notes.tail())
print()
print(notes["Final"])
print()
print(notes.iloc[2])
print()
print(notes[1:5])

print()