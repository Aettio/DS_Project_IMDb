# Data science | Project : "Spotify"

## Гайд по проекту

Перед началом:
- "README.txt" - Содержит сам проект с визуализациями. Предпологаеться что читатель и будет смотреть его как основной файл на входе.
- "DataFrames" - Содержит в себе все дата сеты.
- "Images" - Содержит в себе все картинки "README.txt".
- "Code_Visual" - Содержит в себе код для всего визуала.

p.s. Во всём коде дополнительно были сделаны заметки для удобства чтения и понимания.

## Разделы

- Введение
- Задача
- Exploratory Data Analysis (Анализ данных, более подробно можно просмотреть в Code_Visuals.py)
  - Поиск корреляций
  - Визуализации
  - Самые популярные десятилетия
  - Самая популярная песня
  - Особенности песен с годами
- Итог
- Источники

## Введение

Spotify — интернет-сервис потокового аудио (стриминговый), позволяющий легально прослушивать музыкальные композиции, аудиокниги и подкасты, не скачивая их на устройство. Доступен в виде веб-сайта, приложений для всех операционных систем, смартфонов, смарт-устройств и медиа-систем автомобилей. 

### Данные

Файл «data.csv» содержит более 175 000 песен, собранных с помощью Spotify Web API, а также вы можете найти данные, сгруппированные по исполнителю, году или жанру в разделе данных.

![alt text](https://github.com/Aettio/DS_Project_Spotify/blob/main/Images/Spotify_intro.jpg)

## Задача

Свободный анализ.

## EDA (Exploratory Data Analysis)

### Корреляции

![alt text](https://github.com/Aettio/DS_Project_Spotify/blob/main/Images/Корреляции.png)

### Самые популярные десятилетия

![alt text](https://github.com/Aettio/DS_Project_Spotify/blob/main/Images/Популярнгсть_по_десятилетиям.png)

### Самая популярная песня

![alt text](https://github.com/Aettio/DS_Project_Spotify/blob/main/Images/Самая_популярная_песня.png)

### Особенности треков

- Заметка (Проверить другие особенности по корреляции с year)

![alt text](https://github.com/Aettio/DS_Project_Spotify/blob/main/Images/Особенности_по_year.jpeg)

## Loudness

![alt text](https://github.com/Aettio/DS_Project_Spotify/blob/main/Images/loudness_by_year.jpeg)

## Итог

## Источники

- Датасет : https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks
- xgboost документация https://xgboost.readthedocs.io/en/latest/python/python_api.html#module-xgboost.core
