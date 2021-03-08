import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px 
from collections import Counter

sns.set(style="ticks", context="talk")

df = pd.read_csv("data.csv")
df_artist = pd.read_csv("data_by_artist.csv")
df_genres = pd.read_csv("data_by_genres.csv")
df_year = pd.read_csv("data_by_year.csv")
df_w_genres = pd.read_csv("data_w_genres.csv")

df.head()

# Корреляции

sns.set(rc={"figure.figsize":(16,12)})
sns.heatmap(df.corr(), annot = True, cmap = 'viridis', mask = np.triu(df.corr()), annot_kws = {"size":15})

#

sns.set(rc={"figure.figsize":(12,8)})
g_pn = df.groupby("name")['popularity'].sum().sort_values(ascending=False)[:20]
axis = sns.barplot(x = g_pn.index, y = g_pn, palette = 'viridis')
axis.set_title('Самые популярные треки')
axis.set_ylabel('Популярность')
axis.set_xlabel('Трек')
plt.xticks(rotation = 90)

# 

def get_decade(year):
    first_year = int(year/10)*10
    decade = str(first_year)+"s"
    return decade
  
  
sns.set(rc={"figure.figsize":(10,8)})
  
df["decade"] = df["year"].apply(get_decade)

dec_graph = graph_pop = sns.barplot(data = df.sort_values("decade"), y = "decade", x = "popularity", palette = "viridis")
dec_graph.set_title('Самые популярные десятилетия')
dec_graph.set_ylabel('Десятилетие')
dec_graph.set_xlabel('Популярность')

# 

sound_features = ['acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'valence']
fig = px.line(df_year, x = 'year', y = sound_features)
fig.show()
