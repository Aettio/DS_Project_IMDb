# Data science | Project : "Spotify"

## Project guide

Before the beginning:
- "README.txt" - Contains the project itself with visualizations. It is assumed that the reader will view it as the main input file.
- "DataFrames" - Contains all data sets.
- "Images" - Contains all the pictures "README.txt".
- "Code_Visual" - Contains the code for the entire visual.
- "Code_Regression" - Contains the regression algorithm itself.

p.s. Additional notes have been made throughout the code for ease of reading and understanding.

## Sections

- Introduction
- A task
- Exploratory Data Analysis (Data analysis, more details can be viewed in Code_Visuals.py)
  - Correlations
  - Most Popular Decades
  - Most popular tracks
  - Track features by year
  - Loudness
- Regression
- Total
- Sources

## Introduction

Spotify is an online audio streaming service (streaming) that allows you to legally listen to music, audio books and podcasts without downloading them to your device. Available as a website, applications for all operating systems, smartphones, smart devices and car media systems.

### Data

The "data.csv" file contains more than 175,000 songs collected using Spotify Web API, and you can also find the data grouped by artist, year or genre in the data section.

![alt text](https://github.com/Aettio/DS_Project_Spotify/blob/main/Images/Spotify_intro.jpg)

## A task

Free analysis and practice with the xgboost library.

## EDA (Exploratory Data Analysis)

In this section, we highlight the main dependencies and relationships. You also need to make sure that they make sense. To start the analysis, I chose a graph to visualize correlations.

### Correlations

Here you can see a lot of interesting relationships that are worth checking. We are mainly interested in correlations with "year".

![alt text](https://github.com/Aettio/DS_Project_Spotify/blob/main/Images/Корреляции.png)

### Most Popular Decades

As these tracks of the 90s and 00s have shown, they were and are the most popular decades and they brought to the world many songs that are still considered a kind of classic of the musical genre to this day.

![alt text](https://github.com/Aettio/DS_Project_Spotify/blob/main/Images/Популярнгсть_по_десятилетиям.png)

### Most Played Tracks

It turned out quite interestingly, we have the top of the Christmas tracks that are considered classics and apparently because of their repetition on an annual basis, they manage to hold the top positions for so many years.

![alt text](https://github.com/Aettio/DS_Project_Spotify/blob/main/Images/Самая_популярная_песня.png)

### Features of tracks by year

As you can see, over the years, other types of music that were more energetic and danceable gained popularity.

![alt text](https://github.com/Aettio/DS_Project_Spotify/blob/main/Images/Особенности_по_year.jpeg)

### Loudness

As you can see over the years, the tracks are getting louder, judging by the correlation, this is mainly due to the greater popularity of the genres in which "energy" and "dancebility" appear, as a result of which "Loudness" also shows an increase.

![alt text](https://github.com/Aettio/DS_Project_Spotify/blob/main/Images/loudness_by_year.jpeg)

## Regression

Our goal will be to predict the "feature" of the year using all other numerical variables.

Here everything is according to the standard, after splitting the sample into training and test, we train on the selected data. Then we predict our test set. Then we output Model Score + - 74 and Cross Value Score + - 72.
(More details in Code_Regression.py)

## Total

Now, with our regression, we can determine the "feature" of the year using the numerical variables of the date set. We also conducted a small analysis and tracked the general changes and trends in the development of music over the years, and also identified the most popular tracks, as well as decades. It's safe to say that the music is generally more danceable and energetic, and the volume is also higher. I suppose that one of the main reasons for this was the development of the "Rap" and "Trap" direction, since they use a very large number of basses. It is also worth noting that dance music has also become more popular since the 90s, which in turn greatly influenced the development of dance music, although the genre has changed dramatically.

## Sources

- Dataset : https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks
- xgboost documentation https://xgboost.readthedocs.io/en/latest/python/python_api.html#module-xgboost.core
- Seaborn documentation : https://seaborn.pydata.org/introduction.html
- Pandas documentation : https://pandas.pydata.org/pandas-docs/stable/reference/frame.html
