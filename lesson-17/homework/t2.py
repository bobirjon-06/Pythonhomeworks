import pandas as pd

def classify_age(age):
    return "child" if age < 18 else "adult"

def process_titanic(csv_path="titanic.csv"):
    titanic_df = pd.read_csv(csv_path)
    titanic_df['age_Group'] = titanic_df['age'].apply(classify_age)
    return titanic_df.head()

def classify_duration(minutes):
    if minutes < 60:
        return "Short"
    elif 60 <= minutes <= 120:
        return "Medium"
    else:
        return "Long"

def process_movies(csv_path="movie.csv"):
    movie_df = pd.read_csv(csv_path)
    movie_df['Duration_Category'] = movie_df['duration'].apply(classify_duration)
    return movie_df[['title', 'duration', 'Duration_Category']].head()


try:
    print("age group classification:")
    print(process_titanic())
except Exception as e:
    print("errorr:", e)


try:
    print("movie duration:")
    print(process_movies)
except Exception as e:
    print("error", e) 