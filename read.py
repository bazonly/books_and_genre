import pandas as pd

df = pd.read_csv("books.csv",
                 delimiter=";",
                 names=['Автор', 'Название', 'Жанр'],
                 index_col=None)
genre_df = df['Жанр'].unique()
for genre in genre_df:
    print(genre)