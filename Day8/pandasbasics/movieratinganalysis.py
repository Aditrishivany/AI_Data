import pandas as pd
data={
    "Movie":["Dhurandar","Baazigar","Devdas","Kabhi kushi kabhi gham"],
    "genre":["Action", "Comedy", "Drama","Thriller"],
    "ratings":[4,4,3,5]
}
df=pd.DataFrame(data)
print(df)
#Averagre rating
print("Avg Rating:",df["ratings"].mean())
#top rated movie
top_movies=df[df["ratings"]>=4.5]
print(top_movies)
#low rated movies
df["need_imporv"]=df["ratings"]<3.5
print(df)