
import pandas as pd

data1 = {
        'id':[1,2,3,4],
        'name':["beyza","tala","ayse","muammer"],
        'lastname':["çakmak","cakmak","cakmk","ckmk"]
        }
data2 = {
        'id':[1,3,4,7],
        'name':["aa","bb","cc","dd"],
        'lastname':["a11","b22","c33","d44"]
        }

data1Df = pd.DataFrame(data1)
data2Df = pd.DataFrame(data2)

print(data1Df)
print(data2Df)

print(pd.merge(data1Df,data2Df,on='id',how='inner'))
print()
print(pd.merge(data1Df,data2Df,on='id',how='left'))
print()
print(pd.merge(data1Df,data2Df,on='id',how='right'))
print()
print(pd.concat([data1Df,data2Df],axis=1))



