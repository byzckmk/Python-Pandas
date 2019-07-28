
import pandas as pd

data =  [10,20,30,40,50]
df = pd.DataFrame(data)

print(df)
print()

data2 = [["beyza",23,"konya"],["tala",52,"konya"],["ayşe",44,"konya"]]
df2 = pd.DataFrame(data2,columns=["name","age","city"],index=[1,2,3])

print(df2)
print()

data3 = {"name":["beyza","tala","ayşe"],
         "age":[23,52,44],
         "city":["konya","konya","konya"]}
df3 = pd.DataFrame(data3,columns=["name","age","city"],index=["person1","person2","person3"])

print(df3)
print()
print(df3["name"])
print()
print(df3["age"])
print()

#del df3["city"] # <=> df3.pop("city")
#df3.pop("city") # <=> del df3["city"]
print(df3)
print()

data4 = {"name":["beyza","tala","ayşe"],
         "age":[23,52,44],
         "city":["konya","konya","konya"]}
df4 = pd.DataFrame(data4,columns=["name","age","city"],index=[1,2,3])

print(df4)
print()
print(df4.loc[2])
print()
print(df4.iloc[1]) # integer location starts 0 not index number
print()

df5 = df4.append(df2)
print(df5)
print()
print(df5.head())
print()
print(df5.tail())


















