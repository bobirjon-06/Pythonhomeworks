import sqlite3
import pandas as pd

conn = sqlite3.connect("chinook.db")  
query = "SELECT * FROM customers"  
df_customers = pd.read_sql(query, conn)  
conn.close()

print(df_customers.head(10)) 

df_iris = pd.read_json("iris.json")  
print(df_iris.shape)  
print(df_iris.columns)

iris_df = pd.read_json("iris.json")
iris_df.columns = iris_df.columns.str.lower()
iris_selected = iris_df[['sepal_length', 'sepal_width']]
print(iris_selected.head())

df_titanic = pd.read_excel("titanic.xlsx")  
print(df_titanic.head())
titanic_df = pd.read_excel("titanic.xlsx")
titanic_filtered = titanic_df[titanic_df["age"] > 30]
gender_counts = titanic_df["sex"].value_counts() 
print(gender_counts)

df_flights = pd.read_parquet("Flights.parquet")  
print(df_flights.info())  

df_movies = pd.read_csv("movie.csv")  
print(df_movies.sample(10))

movies_df = pd.read_csv("movie.csv")
movies_filtered = movies_df[movies_df["duration"] > 120]
movies_sorted = movies_filtered.sort_values(by="director_facebook_likes", ascending=False)  
print(movies_sorted.head())