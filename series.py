
import pandas as pd
import numpy as np

data = np.array(["Beyza","Tala","Ayse"])
s = pd.Series(data,index=[1,2,3]) # s = pd.Series(data,index)
print(s)
print(s[1])
print()

data2 = {"mathematics":10, "physics":20, "chemistry":100}
s2 = pd.Series(data2,index=["mathematics","chemistry","physics"])
print(s2)
print()

print(s2[1])
print(s2["mathematics"])
print()

s3 = pd.Series(5,index=[1,2,3,4])
print(s3)
print()