import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import cross_val_score, train_test_split, GridSearchCV

df = pd.read_csv("data.csv")

X = df[['acousticness', 'danceability', 'duration_ms', 'energy', 'explicit', 
        'instrumentalness', 'key', 'liveness', 'loudness', 'mode', 'popularity', 'speechiness',
        'tempo', 'valence']]
y = df['year']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 

model = XGBRegressor()
model.fit(X_train, y_train)

print('Model Check')
print('Model score:', model.score(X_test, y_test))
print('CVS:', cross_val_score(model, X_test, y_test).mean())
