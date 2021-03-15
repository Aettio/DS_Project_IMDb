import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import cross_val_score, train_test_split, GridSearchCV

df = pd.read_csv("data.csv")

# Убираем целевой столбец:

X = df[['acousticness', 'danceability', 'duration_ms', 'energy', 'explicit', 
        'instrumentalness', 'key', 'liveness', 'loudness', 'mode', 'popularity', 'speechiness',
        'tempo', 'valence']]
y = df['year']

# Разбиваем выборку на тренировочную и тестовую:

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Создание:

model = XGBRegressor()

# Тренировка на выбраных данных:

model.fit(X_train, y_train)

# Смотрим оценку и CSV:

print('Model Check')
print('Model score:', model.score(X_test, y_test))
print('CVS:', cross_val_score(model, X_test, y_test).mean())
