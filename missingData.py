
import pandas as pd

url = 'http://bit.ly/uforeports'

data = pd.read_csv(url)
print(data)

print(data.columns)
print(data[["City",
            "Colors Reported",
            "Shape Reported",
            "State",
            "Time"]].head())
print(data.isnull().head(100))
print(data.notnull().head(100))
print(data.isnull().sum())
print(data[data.City.isnull()])

print(data.shape)
#data = data.dropna(how = "all") # (delete missing data row) -> (any: minimum 1 missing data / all:all data missing)
#data = data.dropna(
#        subset=["City","Colors Reported"],
#        how="any")


data['Shape Reported'].fillna(value="Uncertain",inplace=True)
print(data['Shape Reported'].value_counts(dropna=False))


print(data.shape)
























