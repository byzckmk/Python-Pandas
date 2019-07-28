
import pandas as pd

films = pd.read_csv("imdb-1000.csv")

print(films)
print(films.columns)
print(films.head())
print(films.tail())
print(films['title'].head())
print(films.title.head())
print(films[['title','star_rating']].head())
print(films[:9][['title','star_rating']].head())
print()

print(films[films['star_rating']>8.5][['title','star_rating']])
print()
print(
      films[['title','star_rating']][
        (films['star_rating']>=8.5)&(films['star_rating']<=9)
        ])
print()
print(
      films[
        (films['star_rating']>=9)|(films['star_rating']<=7.4)
        ][['title','star_rating']])

print(films.query('star_rating>=9.0 & star_rating <= 9.2')
        [['title','star_rating']])























